Name:      wstx
Version:   3.2.6
Release:        4%{?dist}
Summary:       Woodstox is a high-performance XML processor that implements Stax (JSR-173) API 

Group:         Development/Java
License:        GNU Lesser General Public License (LGPL), Version 2.1
URL:            http://woodstox.codehaus.org
Source0:        wstx-lgpl-3.2.6-sources.jar
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: java-devel  
BuildRequires: jpackage-utils
BuildRequires: msv
BuildRequires: relaxngDatatype
BuildArch: noarch
Requires:  java >= 1.5
Requires:  jpackage-utils
Requires: stax-api = 1.0.1
Provides: wstx-asl
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
mkdir classes javadoc
jar -xf %{SOURCE0}

%build

classpath=$(build-classpath relaxngDatatype msv):src/java 
javac -d classes -cp $classpath `find src/java -name *.java` 
javadoc -d javadoc/ -classpath %{_javadir}/relaxngDatatype.jar:%{_javadir}/msv.jar:src/java  $(for JAVA in `find src/java -name *.java` ; do  dirname $JAVA ; done | sort -u  | sed -e 's!src/java.!!'  -e 's!/!.!g'  )
find classes -name *.class | sed -e  's!classes/!!g' -e 's!^! -C classes !'  | xargs jar cf wstx-3.2.6.jar


%install
#rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
install -m 755 -d $RPM_BUILD_ROOT%{_javadir}
install -m 755    wstx-3.2.6.jar  $RPM_BUILD_ROOT%{_javadir} 
install -m 755 -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp javadoc/*  $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%add_to_maven_depmap org.codehaus.jettison %{name} %{version} JPP %{name}

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
%doc
%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}


%changelog
* Mon Apr 19 2010 Adam Young <ayoung@redhat.com>
- Added JPP Maven Repository Fragment


* Sun Apr 03 2010 Adam Young ayoung@redhat.com
- Specfile Created by pom2rpm by Adam Young ayoung@redhat.com 

