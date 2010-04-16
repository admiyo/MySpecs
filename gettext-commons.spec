Name:           gettext-commons
Version:        0.9.6
Release:        1%{?dist}
Summary:        A Java library that for gettext-based internationalization

Group:          Development/Java
License:        Apache License 2.0
URL:           http://gettext-commons.googlecode.com/
Source0:       http://gettext-commons.googlecode.com/files/gettext-commons-0.9.6-src.tar.gz 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:    junit
BuildRequires:    maven2-plugin-compiler
BuildRequires:    maven2-plugin-install
BuildRequires:    maven2-plugin-jar
BuildRequires:    maven2-plugin-javadoc
#BuildRequires:    maven2-plugin-release
BuildRequires:    maven2-plugin-resources
BuildRequires:    maven2-plugin-surefire
BuildRequires:    maven-surefire-provider-junit
BuildRequires:    maven-doxia-sitetools

%description
The Gettext Commons project provides Java classes for internationalization (i18n) through GNU gettext.

The lightweight library combines the power of the unix-style gettext tools with the widely used Java ResourceBundles. This makes it possible to use the original text instead of arbitrary property keys, which is less cumbersome and makes programs easier to read. And there are a lot more advantages of using gettext:
Easy extraction of user visible strings
Strings are marked as fuzzy when the original text changes so translators can check if the translations still match
Powerful plural handling
Build process integration through Maven or Ant 
%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Documentation
Requires:       %{name}-%{version}-%{release}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q


%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

mvn-jpp \
-Dmaven.repo.local=$MAVEN_REPO_LOCAL \
install javadoc:javadoc

%install
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p   target/%{name}-%{version}.jar \
$RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar


mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/  \
$RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644  .m2/repository/org/xnap/commons/%{name}/%{version}/%{name}-%{version}.pom   \
$RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

%add_to_maven_depmap org.apache.maven %{name} %{version} JPP %{name}


%clean
rm -rf $RPM_BUILD_ROOT
%post
%update_maven_depmap

%postun
%update_maven_depmap

%files
%defattr(-,root,root,-)
%{_datadir}/maven2/poms
%{_mavendepmapfragdir}
%{_javadir}/*
%doc

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}


%changelog
* Fri Apr 16 2010 Adam Young ayoung@redhat.com
- Specfile Created by Adam Young from rpmdev-newspec
- customized based on http://fedoraproject.org/wiki/Packaging/Java

