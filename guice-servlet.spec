Name:      guice-servlet
Version:   2.0
Release:   2%{?dist}
Summary:   extension for guice 
Group:         Development/Java
License:        GPL
URL:            http://code.google.com/p/google-guice/
Source0:        %{name}-%{version}-src.jar
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: java-devel  
BuildRequires:  jpackage-utils
BuildRequires:  guice
BuildRequires: /usr/share/java/servletapi5.jar

BuildArch: noarch
Requires:  java >= 1.5
Requires:  jpackage-utils
Requires: guice
Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils
%description
extension for guice
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
javac -d classes -cp src/:%{_javadir}/guice.jar:%{_javadir}/servletapi5.jar `find . -name *.java` 
javadoc -d javadoc -classpath src/:%{_javadir}/guice.jar:%{_javadir}/servletapi5.jar  $(for JAVA in `find src/ -name *.java` ; do  dirname $JAVA ; done | sort -u  | sed -e 's!src.!!'  -e 's!/!.!g'  )
find classes -name *.class | sed -e  's!classes/!!g' -e 's!^! -C classes !'  | xargs jar cf  %{name}-%{version}.jar

%install
#rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
install -m 755 -d $RPM_BUILD_ROOT%{_javadir}
install -m 755 %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -s %{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -m 755 -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp javadoc/*  $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%add_to_maven_depmap com.google.inject.extensions %{name} %{version} JPP %{name}

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
* Tue Apr 20 2010 Adam Young <ayoung@redhat.com>
- Added JPP Maven Repository support


* Sun Apr 03 2010 Adam Young ayoung@redhat.com
- Specfile Created by pom2rpm by Adam Young ayoung@redhat.com 

