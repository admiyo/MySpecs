# Copyright (c) 2000-2007, JPackage Project
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

%global _with_gcj_support 1

%global gcj_support %{?_with_gcj_support:1}%{!?_with_gcj_support:%{?_without_gcj_support:0}%{!?_without_gcj_support:%{?_gcj_support:%{_gcj_support}}%{!?_gcj_support:0}}}

%global base_name  codec
%global short_name commons-%{base_name}
%global section    free

Name:           jakarta-commons-codec
Version:        1.4
Release:        11.8%{?dist}
Summary:        Implementations of common encoders and decoders
License:        ASL 2.0
Group:          Development/Libraries/Java
Epoch:          0
URL:            http://jakarta.apache.org/commons/codec/
Source0:        commons-codec-%{version}-src.tar.gz
# svn export http://svn.apache.org/repos/asf/jakarta/commons/proper/codec/tags/CODEC_1_3/
# cd CODEC_1_3
# tar czvf commons-codec-1.3-src.tar.gz .

#Patch0:         jakarta-commons-codec-1.3-buildscript.patch
# Add OSGi manifest
Patch1:         %{name}-addosgimanifest.patch
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  ant >= 0:1.6.2
BuildRequires:  ant-junit
BuildRequires:  junit
BuildRequires:  java-javadoc
%if ! %{gcj_support}
BuildArch:      noarch
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Provides:       %{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name} <= %{epoch}:%{version}-%{release}

%if %{gcj_support}
BuildRequires:          java-gcj-compat-devel
Requires(post):         java-gcj-compat
Requires(postun):       java-gcj-compat
%endif

Requires:       jpackage-utils

Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils



%description
Commons Codec is an attempt to provide definitive implementations of
commonly used encoders and decoders. Examples include Base64, Hex,
Phonetic and URLs.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       java-javadoc

%description    javadoc
Javadoc for %{name}.

# -----------------------------------------------------------------------------

%prep
%setup -q -n commons-codec-1.4-src

#was -q -c

# FIXME Remove SoundexTest which is failing
# and thus preventing the build to proceed.
# This problem has been communicated upstream Bug 31096
#%patch0 -p1

# Add OSGi manifest
#pushd src/conf
#%patch1 -p0
#popd

#fixes eof encoding
#%{__sed} -i 's/\r//' LICENSE.txt
#%{__sed} -i 's/\r//' RELEASE-NOTES.txt

# -----------------------------------------------------------------------------

%build

export CLASSPATH=$(build-classpath junit)
#perl -p -i -e 's|../LICENSE|LICENSE.txt|g' build.xml
ant -Dbuild.sysclasspath=first \
  -Dconf.home=src/conf \
  -Dbuild.home=build \
  -Dsource.home=src/java \
  -Dtest.home=src/test \
  -Ddist.home=dist \
  -Dcomponent.title=%{short_name} \
  -Dcomponent.version=%{version} \
  -Dfinal.name=%{name}-%{version} \
  -Dextension.name=%{short_name} \
  test jar javadoc

# -----------------------------------------------------------------------------

%install
rm -rf $RPM_BUILD_ROOT

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|jakarta-||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

%add_to_maven_depmap org.apache.commons.commons-codec %{name} %{version} JPP %{name}
%add_to_maven_depmap commons-codec commons-codec %{version} JPP %{name}

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# -----------------------------------------------------------------------------

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%clean
rm -rf $RPM_BUILD_ROOT

# -----------------------------------------------------------------------------

%if %{gcj_support}
%post
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif
%update_maven_depmap





%if %{gcj_support}
%postun
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif
%update_maven_depmap

%files
%defattr(0644,root,root,0755)
%doc LICENSE.txt RELEASE-NOTES.txt
%{_javadir}/*
%{_mavendepmapfragdir}

%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/jakarta-commons-codec-%{version}.jar.*
%endif

%files javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}
# -----------------------------------------------------------------------------

%changelog
* Mon Apr 19 2010 Adam Young <ayoung@redhat.com>
- Added JPP Maven Repository Fragment

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.3-11.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.3-10.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 24 2008 Andrew Overholt <overholt@redhat.com> 1.3-9.4
- Update OSGi manifest.

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:1.3-9.3
- drop repotag
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0:1.3-9jpp.2
- Autorebuild for GCC 4.3

* Thu Sep 06 2007 Andrew Overholt <overholt@redhat.com> 1.3-8jpp.2
- Add OSGi manifest.

* Wed Mar 21 2007 Matt Wringe <mwringe@redhat.com> 0:1.3-8jpp.1
- Update to latest jpp version
- Fix rpmlint issues

* Wed Mar 21 2007 Matt Wringe <mwringe@redhat.com> 0:1.3-8jpp
- Fix some rpmlint warnings
- Update copyright year

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> 0:1.3-7jpp.2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 26 2006 Matt Wringe <mwringe at redhat.com> 0:1.3-7jpp.1
- Merge with upstream version.

* Tue Sep 26 2006 Matt Wringe <mwringe at redhat.com> 0:1.3-7jpp
- Add missing java-javadoc requires and buildrequires.

* Mon Sep 25 2006 Matt Wringe <mwringe at redhat.com> 0:1.3-6jpp.1
- Merge with upstream version.

* Mon Sep 25 2006 Matt Wringe <mwringe at redhat.com> 0:1.3-6jpp
- Update jakarta-commons-codec-1.3-buildscript.patch to build
  offline.

* Thu Aug 10 2006 Matt Wringe <mwringe at redhat.com> 0:1.3-5jpp.1
- Merge with upstream version
 - Add missing javadoc requires

* Sat Jul 22 2006 Jakub Jelinek <jakub@redhat.com> - 0:1.3-4jpp_2fc
- Rebuilt

* Thu Jul 20 2006 Matt Wringe <mwringe at redhat.com> 0:1.3-4jpp_1fc
- Merged with upstream version
- Now is natively compiled

* Thu Jul 20 2006 Matt Wringe <mwringe at redhat.com> 0:1.3-4jpp
- Added conditional native compiling

* Tue Apr 04 2006 Ralph Apel <r.apel@r-apel.de> 0:1.3-3jpp
- First JPP-1.7 release

* Wed Sep 08 2004 Fernando Nasser <fnasser@redhat.com> 0:1.3-2jpp
- Do not stop on test failure

* Tue Sep 07 2004 Fernando Nasser <fnasser@redhat.com> 0:1.3-1jpp
- Upgrade to 1.3
- Rebuilt with Ant 1.6.2

* Thu Jan 22 2004 David Walluck <david@anti-microsoft.org> 0:1.2-1jpp
- 1.2
- use perl instead of patch

* Wed May 28 2003 Ville Skyttä <jpackage-discuss at zarb.org> - 0:1.1-1jpp
- First JPackage release.
