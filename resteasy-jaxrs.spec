Name:      resteasy-jaxrs
Version:   1.2.1.GA
Release:        4%{?dist}
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
BuildRequires: servletapi5
BuildRequires: junit
BuildRequires: slf4j
BuildRequires: scannotation
BuildRequires: activation
BuildRequires: commons-httpclient
BuildRequires: httpclient

Requires: jaxrs-api = %{version}
Requires: servletapi5
Requires: slf4j
Requires: activation
Requires: commons-httpclient
Requires: httpclient

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
rm -rf org/jboss/resteasy/plugins/server/tjws/
rm -rf  org/jboss/resteasy/test
popd



%build

classpath=src/:$(build-classpath  jaxrs-api servletapi5 junit slf4j/api scannotation activation commons-httpclient httpcore httpclient annotation_api)

javac -d classes -cp $classpath `find . -name *.java` 

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
/etc/maven/fragments/%{name}
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

