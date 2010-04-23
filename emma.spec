# Copyright (c) 2000-2008, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define gcj_support %{?_with_gcj_support:1}%{!?_with_gcj_support:%{?_without_gcj_support:0}%{!?_without_gcj_support:%{?_gcj_support:%{_gcj_support}}%{!?_gcj_support:0}}}

%define section         free

Name:           emma
Version:        2.0
Release:        0.5312.5%{?dist}
Epoch:          0
Summary:        Code Coverage Tool
Group:          Development/Testing
License:        CPL
URL:            http://emma.sourceforge.net/
Source0:        emma-2.0.5312-src.zip
Source1:        emma-2.0.5312.pom
Source2:        emma_ant-2.0.5312.pom
Patch0:         emma-2.0.5312-dependencies_xml.patch
Patch1:         emma-2.0.5312-build_xml.patch
Patch2:         emma-2.0.5312-no-version-stamp-tool.patch
Patch3:         emma-2.0.5312-no-javac-target.patch
Patch4:         emma-2.0.5312-code-source.patch
Requires:       jaxp_parser_impl
Requires(post): jpackage-utils >= 0:1.7.2
Requires(postun): jpackage-utils >= 0:1.7.2
BuildRequires:  ant
BuildRequires:  java-devel
BuildRequires:  jpackage-utils
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
EMMA is an open-source toolkit for measuring and reporting Java 
code coverage. EMMA distinguishes itself from other tools by going 
after a unique feature combination: support for large-scale 
enterprise software development while keeping individual developer's 
work fast and iterative. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{version}.5312
%patch0
%patch1
rm core/data/com/vladium/app/IAppVersion.java
%patch2 -p1
%patch3 -p1
%patch4 -p1
find . -name "*.jar" | xargs rm

%build
export CLASSPATH=
export OPT_JAR_LIST=:
ant build javadoc

%install
rm -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/%{name}.jar \
               $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 dist/%{name}_ant.jar \
               $RPM_BUILD_ROOT%{_javadir}/%{name}_ant-%{version}.jar
%add_to_maven_depmap emma emma %{version} JPP %{name}
%add_to_maven_depmap emma emma_ant %{version} JPP %{name}_ant
%add_to_maven_depmap emma emma %{version}.5312 JPP %{name}
%add_to_maven_depmap emma emma_ant %{version}.5312 JPP %{name}_ant

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}.pom
install -pm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}_ant.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr out/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_maven_depmap
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%postun
%update_maven_depmap 
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%files
%defattr(0644,root,root,0755)
%doc cpl-v10.html
%{_javadir}/*
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}*%{version}.jar.*
%endif

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Tue Jul 29 2008 David Walluck <dwalluck@redhat.com> 0:2.0-0.5312.4
- patch to remove binary jar
- patch to fix build

* Tue Jul 29 2008 David Walluck <dwalluck@redhat.com> 0:2.0-0.5312.3
- build for JPackage 5

* Fri Jul 06 2007 Ralph Apel <r.apel at r-apel.de> 0:2.0-0.5312.2jpp
- Make Vendor, Distribution based on macro
- Add -javadoc subpackage
- Add gcj_support option
- Add poms and depmap frags

* Wed Feb 01 2006 Ralph Apel <r.apel at r-apel.de> 0:2.0-0.5312.1jpp
- First JPackage release.

