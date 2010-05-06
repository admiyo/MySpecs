# Copyright (c) 2000-2009, JPackage Project
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

%global section free
%global namedversion 3.1.0.GA

%global reltag  SP1_CP01

Name:           hibernate3-validator
Version:        3.1.0
Release:        2%{?dist}
Epoch:          0
Summary:        Bean validator
License:        LGPLv2+
URL:            http://www.hibernate.org/
Group:          Database
# svn export http://anonsvn.jboss.org/repos/hibernate/validator/tags/3.1.0.GA/ hibernate3-validator-3.1.0.GA
Source0:        hibernate3-validator-3.1.0.GA.tar.gz
Source1:        %{name}-jpp-depmap.xml
Source2:        %{name}-settings.xml
Patch0:         hibernate3-validator-pom.patch
Patch1:         hibernate3-validator-pom2.patch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires:       java >= 0:1.5.0
Requires:       hibernate3
Requires:       hibernate3-commons-annotations
Requires:       hibernate3-annotations
Requires:       hibernate3-ejb-persistence-3.0-api
Requires:       hibernate3-entitymanager
Requires:       slf4j
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  hibernate3
BuildRequires:  hibernate3-commons-annotations
BuildRequires:  hibernate3-annotations
BuildRequires:  hibernate3-ejb-persistence-3.0-api
BuildRequires:  hibernate3-entitymanager
BuildRequires:  java-devel >= 0:1.5.0
BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  junit >= 0:3.8.1
BuildRequires:  maven2 >= 0:2.0.7
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  slf4j
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Following the DRY (Don't Repeat Yourself) principle, 
Hibernate Validator let's you express your domain 
constraints once (and only once) and ensure their 
compliance at various level of your system 
automatically.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n hibernate3-validator-3.1.0.GA
%patch0 -b .sav0
%patch1 -b .sav1

cp -p %{SOURCE2} maven2-settings.xml

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

%build
export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=`pwd`/m2_repo/repository
export MAVEN_OPTS="-Xmx384m -Dmaven.repo.local=$MAVEN_REPO_LOCAL -Dmaven2.jpp.depmap.file=%{SOURCE1}"
%{_bindir}/mvn-jpp -e \
        -s ${M2SETTINGS} \
        install javadoc:javadoc

%install
rm -rf %{buildroot}

# jars
mkdir -p %{buildroot}%{_javadir}/%{name}
install -p -m 644 target/hibernate-validator-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# poms
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -m 644 pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.hibernate hibernate-validator %{namedversion} JPP %{name}

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%clean
rm -rf %{buildroot}

%post
%update_maven_depmap

%postun
%update_maven_depmap

%files
%defattr(0644,root,root,0755)
%doc lgpl.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Fri Nov 13 2009 David Walluck <dwalluck@redhat.com> 0:3.1.0-2
- 3.1.0.GA

* Mon Aug 31 2009 Ralph Apel <r.apel@r-apel.de> 0:3.1.0-1
- first release
