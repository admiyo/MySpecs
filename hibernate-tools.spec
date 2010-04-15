Name:      hibernate-tools
Version:   3.2.4.GA
Release:        2%{?dist}
Summary:       Forward- and reverse-engineering tools for Eclipse and Ant. 

Group:         Development/Java
License:        GNU LESSER GENERAL PUBLIC LICENSE
URL:            http://tools.hibernate.org
Source0:        %{name}-%{version}-sources.jar
Patch0:         %{name}-cachefactory.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch

BuildRequires: java-devel  
BuildRequires: jpackage-utils
BuildRequires: hibernate3
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-commons-collections
BuildRequires: antlr
BuildRequires: dom4j
BuildRequires: cglib
#BuildRequires: ehcache


Requires: java >= 1.5
Requires: jpackage-utils
Requires: bsh >= 2.0b4
Requires: freemarker >= 2.3.8
Requires: jtidy> = r8-20060801
Requires: jakarta-commons-logging
Requires: jakarta-commons-collections
Requires: hibernate3
Requires: antlr
Requires: dom4j
Requires: cglib


%description
#%package javadoc
#Summary:        Javadocs for %{name}
#Group:          Development/Documentation
#Requires:       %{name} = %{version}-%{release}
#Requires:       jpackage-utils

#%description javadoc
#This package contains the API documentation for %{name}.

%prep
%setup -cT
patch -p0 <  %{PATCH0}
mkdir src javadoc classes
pushd src
jar -xf %{SOURCE0}
popd

%build


classpath=src/:$(build-classpath   commons-logging freemarker hibernate-core jakarta-commons-logging jakarta-commons-logging-jboss slf4j/jcl-over-slf4j jpa_api persistence-api javassist hibernate3-ejb-persistence-3.0-api ant jboss-common-core hibernate-annotations hibernate3-annotations dom4j cglib commons-collections jtidy jta.jar )

#classpath=src/:$(build-classpath bsh.jar freemarker.jar jtidy.jar hibernate-core.jar jakarta-commons-logging.jar jakarta-commons-collections.jar ant antlr dom4j cglib lucene jms_api jta_api javassist jboss-common-core jpa_api ):/usr/lib64/eclipse/plugins/org.eclipse.text_3.5.0.v20090513-2000.jar:/usr/lib64/eclipse/plugins/org.eclipse.jface.text_3.5.1.r351_v20090708-0800.jar:/usr/lib64/eclipse/dropins/jdt/plugins/org.eclipse.jdt.core_3.5.1.v_972_R35x.jar



javac -d classes -cp $classpath  `find . -name *.java` 
javadoc -d javadoc -classpath $classpath $(for JAVA in `find src/ -name *.java` ; do  dirname $JAVA ; done | sort -u  | sed -e 's!src.!!'  -e 's!/!.!g'  )
find classes -name *.class | sed -e  's!classes/!!g' -e 's!^! -C classes !'  | xargs jar cfm %{name}-%{version}.jar ./src/META-INF/MANIFEST.MF


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
install -m 755 -d $RPM_BUILD_ROOT%{_javadir}
install -m 755 %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -s %{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
#install -m 755 -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}
#cp -rp javadoc/*  $RPM_BUILD_ROOT%{_javadocdir}/%{name}

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
#%files javadoc
#%defattr(-,root,root,-)
#%{_javadocdir}/%{name}


%changelog
* Sun Apr 03 2010 Adam Young ayoung@redhat.com
- Specfile Created by pom2rpm by Adam Young ayoung@redhat.com 

