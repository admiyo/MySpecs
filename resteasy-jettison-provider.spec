Name:      resteasy-jettison-provider
Version:   1.2.1.GA
Release:        2%{?dist}
Summary:       Resteasy Jettison Provider 

Group:         Development/Java
License:        GPL
URL:            http://repository.jboss.org/maven2/org/jboss/resteasy/resteasy-jettison-provider/1.2.1.GA/
Source0:        %{name}-%{version}-sources.jar
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: java-devel  
BuildRequires:  jpackage-utils
BuildArch: noarch
BuildRequires: resteasy-jaxrs >= ${project.version}
BuildRequires: resteasy-jaxb-provider >= ${project.version}
BuildRequires: jettison = 1.1
BuildRequires: servletapi5
BuildRequires: junit
BuildRequires: jaxrs-api

Requires:  java >= 1.5
Requires:  jpackage-utils
Requires: resteasy-jaxrs >= ${project.version}
Requires: resteasy-jaxb-provider >= ${project.version}
Requires: jettison = 1.1
Requires: servletapi5
Requires: jaxrs-api

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
classpath=src/:%{_javadir}/resteasy-jaxrs.jar:%{_javadir}/resteasy-jaxb-provider.jar:%{_javadir}/jettison-1.1.jar:%{_javadir}/servletapi5.jar:%{_javadir}/junit.jar::%{_javadir}/jaxrs-api.jar

javac -d classes -cp $classpath  `find . -name *.java` 
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

