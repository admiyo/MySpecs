Name:      jakarta-commons-pool
Version:   1.2
Release:        3%{?dist}
Summary:       Commons Pool 

Group:         Development/Java
License:        The Apache Software License, Version 2.0
URL:            http://jakarta.apache.org/commons/pool/
Source0:        commons-pool-%{version}-sources.jar
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: java-devel  
BuildRequires:  jpackage-utils
BuildArch: noarch
BuildRequires: commons-collections >= 2.1
BuildRequires: junit >= 3.8.1
#BuildRequires: xml-apis >= 2.0.2
#BuildRequires: xerces >= 2.0.2
Requires:  java >= 1.5
Requires:  jpackage-utils
Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils
Requires: commons-collections >= 2.1
Requires: junit >= 3.8.1
#Requires: xml-apis >= 2.0.2
#Requires: xerces >= 2.0.2


%description
%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Documentation
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -cT
mkdir src javadoc classes
pushd src
jar -xf %{SOURCE0}
popd

%build
#classpath=src:$(build-classpath commons-collections junit xml-apis xerces  )
classpath=src:$(build-classpath commons-collections junit xerces-j2  )
javac -source 1.4 -d classes -cp $classpath  `find . -name *.java` 
javadoc -source 1.4 -d javadoc -classpath $classpath  $(for JAVA in `find src/ -name *.java` ; do  dirname $JAVA ; done | sort -u  | sed -e 's!src.!!'  -e 's!/!.!g'  )
find classes -name *.class | sed -e  's!classes/!!g' -e 's!^! -C classes !'  | xargs jar cf %{name}-%{version}.jar 


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
install -m 755 -d $RPM_BUILD_ROOT%{_javadir}
install -m 755 %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
install -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{_javadir}
ln -s %{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -m 755 -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp javadoc/*  $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%add_to_maven_depmap commons-pool commons-pool  %{version} JPP %{name}
%add_to_maven_depmap jakarta-commons-pool %{name} %{version} JPP %{name}
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

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
%{_javadir}/commons-pool-%{version}-sources.jar
%{_javadir}/%{name}.jar
%doc
%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}


%changelog
* Sun Apr 03 2010 Adam Young ayoung@redhat.com
- Specfile Created by pom2rpm by Adam Young ayoung@redhat.com 

