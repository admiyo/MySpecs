Name:      jakarta-commons-dbcp
Version:   1.4
Release:        3%{?dist}
Summary:       Commons DBCP

Group:         Development/Java
License:        The Apache Software License, Version 2.0
URL:            http://jakarta.apache.org/commons/pool/
Source0:        %{name}-%{version}-src.tar.gz
Source1:        %{name}-%{version}-build.properties

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: java-devel  
BuildRequires:  jpackage-utils
BuildArch: noarch
BuildRequires: commons-collections >= 2.1
BuildRequires: junit >= 3.8.1
Requires:  java >= 1.5
Requires:  jpackage-utils
Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils
Requires: commons-collections >= 2.1
Requires: junit >= 3.8.1

%description
%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Documentation
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n commons-dbcp-%{version}-src
cp %{SOURCE1} build.properties


%build
ant dist
cp dist/commons-dbcp.jar dist/jakarta-commons-dbcp.jar

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
install -m 755 -d $RPM_BUILD_ROOT%{_javadir}
install -m 755 dist/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
#install -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{_javadir}
ln -s %{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -m 755 -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp dist/docs/*  $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}
%add_to_maven_depmap commons-dbcp commons-dbcp %{version} JPP commons-dbcp

%clean
rm -rf $RPM_BUILD_ROOT


%post
%update_maven_depmap

%postun
%update_maven_depmap


%files
%defattr(-,root,root,-)
%{_mavendepmapfragdir}
%{_javadir}/%{name}-%{version}.jar
#%{_javadir}/%{name}-%{version}-src.jar
%{_javadir}/%{name}.jar
%doc
%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}


%changelog
* Sun Apr 03 2010 Adam Young ayoung@redhat.com
- Specfile Created by pom2rpm by Adam Young ayoung@redhat.com 

