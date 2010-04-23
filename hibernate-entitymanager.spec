Name:      hibernate-entitymanager
Version:   3.4.0.GA
Release:        1%{?dist}
Summary:       Hibernate Entitity Manager 

Group:         Development/Java
License:        GNU LESSER GENERAL PUBLIC LICENSE
URL:            http://hibernate.org
Source0:        %{name}-%{version}-sources.jar
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: java-devel  
BuildRequires:  jpackage-utils
BuildArch: noarch
BuildRequires: hibernate3-ejb-persistence-3.0-api
BuildRequires: hibernate-commons-annotations 
BuildRequires: hibernate3-annotations        
BuildRequires: hibernate3                    
BuildRequires: slf4j                         
BuildRequires: dom4j                         
BuildRequires: jta                           
BuildRequires: javassist                     
Requires:  java >= 1.5
Requires:  jpackage-utils
Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils
Requires: hibernate3-ejb3-persistence-3.0-api
Requires: hibernate-commons-annotations >= 3.1.0.GA
Requires: hibernate3-annotations >= 3.4.0.GA
Requires: hibernate3
Requires: slf4j-api >= 1.4.2
Requires: dom4j >= 1.6.1
Requires: jta >= 1.1
Requires: javassist >= 3.4.GA

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
classpath=src:$(build-classpath hibernate3-ejb-persistence-3.0-api hibernate-commons-annotations hibernate3-annotations hibernate3-core slf4j dom4j jta javassist  )
javac -d classes -cp $classpath  `find . -name *.java` 
javadoc -d javadoc -classpath $classpath  $(for JAVA in `find src/ -name *.java` ; do  dirname $JAVA ; done | sort -u  | sed -e 's!src.!!'  -e 's!/!.!g'  )
find classes -name *.class | sed -e  's!classes/!!g' -e 's!^! -C classes !'  | xargs jar cfm %{name}-%{version}.jar ./src/META-INF/MANIFEST.MF


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
install -m 755 -d $RPM_BUILD_ROOT%{_javadir}
install -m 755 %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
install -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{_javadir}
ln -s %{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -m 755 -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp javadoc/*  $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%add_to_maven_depmap org.hibernate %{name} %{version} JPP %{name}
%add_to_maven_depmap org.hibernate hibernate3-entitymanager %{version} JPP %{name}

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
%{_javadir}/%{name}-%{version}-sources.jar
%{_javadir}/%{name}.jar
%doc
%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}


%changelog
* Sun Apr 03 2010 Adam Young ayoung@redhat.com
- Specfile Created by pom2rpm by Adam Young ayoung@redhat.com 

