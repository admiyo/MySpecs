Name:      scannotation
Version:   1.0.2
Release:        2%{?dist}
Summary:       scannotation 

Group:         Development/Java
License:        Apache License V2.0
URL:            https://sourceforge.net/projects/scannotation/
Source0:        scannotation-1.0.2.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: java-devel  
BuildRequires:  jpackage-utils
BuildArch: noarch
Requires:  java >= 1.5
Requires:  jpackage-utils
BuildRequires: junit4
BuildRequires: servletapi5
BuildRequires: javassist >= 3.6.0.GA

#BuildRequires: titan-cruise = 1.0
#BuildRequires: javassist = 3.6.0.GA
#Requires: titan-cruise = 1.0
Requires: javassist >= 3.6.0.GA
Requires: servletapi5
%description
%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Documentation
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils
Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup 
mkdir src javadoc classes
mv scannotation/src/main/java/* src


%build
javac -d classes -cp src/:%{_javadir}/persistence-api.jar:%{_javadir}/tomcat6/annotations-api.jar:%{_javadir}/junit4.jar:%{_javadir}/javassist.jar:%{_javadir}/servletapi5.jar   `find . -name *.java` 
javadoc -d javadoc -classpath src/:%{_javadir}/persistence-api.jar:%{_javadir}/tomcat6/annotations-api.jar:%{_javadir}/junit4.jar:%{_javadir}/javassist.jar:%{_javadir}/servletapi5.jar  $(for JAVA in `find src/ -name *.java` ; do  dirname $JAVA ; done | sort -u  | sed -e 's!src.!!'  -e 's!/!.!g'  )
find classes -name *.class | sed -e  's!classes/!!g' -e 's!^! -C classes !'  | xargs jar cf %{name}-%{version}.jar


%install
#rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
install -m 755 -d $RPM_BUILD_ROOT%{_javadir}
install -m 755 %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -s %{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -m 755 -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp javadoc/*  $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%add_to_maven_depmap  org.scannotation %{name} %{version} JPP %{name}

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
%{_javadir}/%{name}.jar
%doc
%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}


%changelog
* Mon Apr 19 2010 Adam Young <ayoung@redhat.com>
- Added JPP Maven Repository Fragment

* Sun Apr 03 2010 Adam Young ayoung@redhat.com
- Specfile Created by pom2rpm by Adam Young ayoung@redhat.com 

