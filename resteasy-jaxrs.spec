Name:      resteasy-jaxrs
Version:   1.2.1.GA
Release:        2%{?dist}
Summary:       RESTEasy JAX-RS Implementation 

Group:         Development/Java
License:        GPL
URL:            http://www.jboss.org/resteasy
Source0:        %{name}-%{version}-sources.jar
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: java-devel  
BuildRequires:  jpackage-utils
BuildArch: noarch
Requires:  java >= 1.5
Requires:  jpackage-utils
BuildRequires: jaxrs-api = %{version}
#BuildRequires: servlet-api
#BuildRequires: junit
BuildRequires: slf4j
BuildRequires: scannotation
BuildRequires: activation
BuildRequires: commons-httpclient
BuildRequires: httpclient

Requires: jaxrs-api = %{version}
Requires: servletapi5
#Requires: junit
Requires: slf4j
Requires: activation
Requires: commons-httpclient
Requires: httpclient

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
rm -rf org/jboss/resteasy/plugins/server/tjws/
rm -rf  org/jboss/resteasy/test
popd



%build

javac -d classes -cp src/:%{_javadir}/jaxrs-api.jar:%{_javadir}/servletapi5.jar:%{_javadir}/junit.jar:%{_javadir}/slf4j/api.jar:%{_javadir}/scannotation.jar:%{_javadir}/jsr250-api.jar:%{_javadir}/activation.jar:%{_javadir}/commons-httpclient.jar:%{_javadir}/httpcore.jar:%{_javadir}/httpclient.jar:%{_javadir}/annotation_api.jar  `find . -name *.java` 

#javac -d classes -cp src/:%{_javadir}/jaxrs-api.jar:%{_javadir}/servletapi5.jar:%{_javadir}/junit.jar:%{_javadir}/slf4j/api.jar:%{_javadir}/slf4j-simple.jar:%{_javadir}/jcl-over-slf4j.jar:%{_javadir}/scannotation.jar:%{_javadir}/jsr250-api.jar:%{_javadir}/activation.jar:%{_javadir}/commons-httpclient.jar:%{_javadir}/httpcore.jar:%{_javadir}/httpclient.jar:%{_javadir}/annotation_api.jar:%{_javadir}/jcip-annotations.jar:%{_javadir}/webserver.jar  `find . -name *.java` 



javadoc -d javadoc -classpath src/:%{_javadir}/jaxrs-api.jar:%{_javadir}/servletapi5.jar:%{_javadir}/junit.jar:%{_javadir}/slf4j/api.jar:%{_javadir}/scannotation.jar:%{_javadir}/jsr250-api.jar:%{_javadir}/activation.jar:%{_javadir}/commons-httpclient.jar:%{_javadir}/httpcore.jar:%{_javadir}/httpclient.jar:%{_javadir}/annotation_api.jar  $(for JAVA in `find src/ -name *.java` ; do  dirname $JAVA ; done | sort -u  | sed -e 's!src.!!'  -e 's!/!.!g'  )
find classes -name *.class | sed -e  's!classes/!!g' -e 's!^! -C classes !'  | xargs jar cfm %{name}-%{version}.jar ./src/META-INF/MANIFEST.MF


%install
#rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
install -m 755 -d $RPM_BUILD_ROOT%{_javadir}
install -m 755 %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -s %{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -m 755 -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp javadoc/*  $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%add_to_maven_depmap org.apache.maven %{name} %{version} JPP %{name}

%clean
rm -rf $RPM_BUILD_ROOT


%post
%update_maven_depmap

%postun
%update_maven_depmap


%files
%defattr(-,root,root,-)
/etc/maven/fragments/%{name}
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%doc
%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}


%changelog
* Sun Apr 03 2010 Adam Young ayoung@redhat.com
- Specfile Created by pom2rpm by Adam Young ayoung@redhat.com 

