Name:      quartz
Version:   1.7.3
Release:        2%{?dist}
Summary:       Quartz Enterprise Job Scheduler 

Group:         Development/Java
License:        GPL
URL:            http://repo2.maven.org/maven2/org/quartz-scheduler/quartz/1.7.3/
Source0:        %{name}-%{version}-sources.jar
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: java-devel  
BuildRequires:  jpackage-utils
BuildArch: noarch
BuildRequires: glassfish-jaf                 
BuildRequires: glassfish-javamail            
BuildRequires: jta                           
BuildRequires: servletapi5
BuildRequires: jakarta-commons-logging       
BuildRequires: jakarta-commons-beanutils     
BuildRequires: jakarta-commons-dbcp          
BuildRequires: jakarta-commons-digester      
BuildRequires: jakarta-commons-pool          
BuildRequires: log4j                         
BuildRequires: junit4                        
BuildRequires:  objectweb-asm      
BuildRequires: geronimo-ejb-3.0-api
Requires:  java >= 1.5
Requires:  jpackage-utils
Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils
Requires: activation >= 1.1
Requires: jta >= 1.0.1B
#Requires: jms >= 1.1
Requires: jakarta-commons-logging >= 1.1
Requires: jakarta-commons-beanutils >= 1.7.0
Requires: jakarta-commons-dbcp >= 1.2.2
Requires: jakarta-commons-digester >= 1.7
#Requires: jakarta-commons-digester >= 1.8.1
Requires: jakarta-commons-modeler >= 2.0
Requires: commons-pool >= 1.3
Requires: jakarta-commons-validator >= 1.1.4
Requires: log4j >= 1.2.14
Requires: junit >= 3.8.1
Requires: objectweb-asm >= 3.1

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
classpath=src:$(build-classpath glassfish-jaf glassfish-javamail-monolithic jta jms servletapi5 ejb_3_0_api  commons-logging commons-beanutils jakarta-commons-dbcp commons-digester commons-modeler jakarta-commons-pool commons-validator log4j junit4  objectweb-asm/asm-all )
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

%add_to_maven_depmap org.quartz-scheduler %{name} %{version} JPP %{name}

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

