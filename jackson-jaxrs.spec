Name:      jackson-jaxrs
Version:   1.4.3
Release:        3%{?dist}
Summary:       JAX-RS provider for JSON content type 

Group:         Development/Java
License:        The Apache Software License, Version 2.0
URL:            http://jackson.codehaus.org
Source0:        %{name}-%{version}-sources.jar
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch

BuildRequires: java-devel  
BuildRequires:  jpackage-utils
BuildRequires: jackson-core-lgpl >= 1.4.1
BuildRequires: jackson-mapper >= 1.4.3
BuildRequires: jackson-xc >= 1.4.3
Requires:  java >= 1.5
Requires:  jpackage-utils
Requires: jackson-core-lgpl >= 1.4.1
Requires: jackson-mapper >= 1.4.3
Requires: jackson-xc >= 1.4.3
Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils

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
classpath=src/:%{_javadir}/jackson-core-lgpl.jar:%{_javadir}/jackson-mapper.jar:%{_javadir}/jaxrs-api.jar:%{_javadir}/jackson-xc.jar
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

%add_to_maven_depmap  org.codehaus.jackson %{name} %{version} JPP %{name}

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

