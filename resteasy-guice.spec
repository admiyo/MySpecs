Name:      resteasy-guice
Version:    1.2.1.GA
Release:        4%{?dist}
Summary:     RESTEasy integration with Guice   

Group:         Development/Java
License:        GPL
URL:            http://www.jboss.org/resteasy
Source0:        %{name}-%{version}-sources.jar
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch

BuildRequires: java-devel  
BuildRequires:  jpackage-utils
BuildRequires: guice = 2.0
BuildRequires: resteasy-jaxrs = %{version}
BuildRequires: junit
BuildRequires: servletapi5
BuildRequires: junit
BuildRequires: jsr311-api 


Requires:  java >= 1.5
Requires:  jpackage-utils
Requires: guice >= 2.0
Requires: resteasy-jaxrs = %{version}
Requires: servletapi5
Requires: jsr311-api 
Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils

%description
RESTEasy has some simple integration with Guice 1.0. RESTEasy will scan the binding types for a Guice Module for @Path and @Provider annotations. It will register these bindings with RESTEasy. The guice-hello project that comes in the RESTEasy examples/ directory gives a nice example of this

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
classpath=src/:$(build-classpath guice resteasy-jaxrs junit servletapi5 jsr311-api slf4j/api)
javac -d classes -cp $classpath   `find . -name *.java` 
javadoc -d javadoc -classpath $classpath  $(for JAVA in `find src/ -name *.java` ; do  dirname $JAVA ; done | sort -u  | sed -e 's!src.!!'  -e 's!/!.!g'  )
find classes -name *.class | sed -e  's!classes/!!g' -e 's!^! -C classes !'  | xargs jar cfm %{name}-%{version}.jar ./src/META-INF/MANIFEST.MF


%install
#rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
install -m 755 -d $RPM_BUILD_ROOT%{_javadir}
install -m 755 %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -s %{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -m 755 -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp javadoc/*  $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%add_to_maven_depmap org.jboss.resteasy %{name} %{version} JPP %{name}

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

