Name:      cglib
Version:   2.2
Release:        2%{?dist}
Summary:        Code Generation Library used to extend JAVA classes and implements interfaces at runtime.

Group:         Development/Java
License:        ASF 2.0
URL:            http://cglib.sourceforge.net/
Source0:        cglib-2.2-sources.jar
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: java-devel  
BuildRequires:  jpackage-utils
BuildArch: noarch
Requires:  java >= 1.5
Requires:  jpackage-utils
Requires: objectweb-asm = 3.1
Requires: ant >= 1.6.2

%description
Code Generation Library used to extend JAVA classes and implements interfaces at runtime.
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
javac -d classes -cp src/:%{_javadir}/objectweb-asm/asm-all.jar:%{_javadir}/ant.jar `find . -name *.java` 
javadoc -d javadoc -classpath src:%{_javadir}/objectweb-asm/asm-all.jar:%{_javadir}/ant.jar  $(for JAVA in `find src/ -name *.java` ; do  dirname $JAVA ; done | sort -u  | sed -e 's!src.!!'  -e 's!/!.!g'  )
find classes -name *.class | sed -e  's!classes/!!g' -e 's!^! -C classes !'  | xargs jar cfm cglib-2.2.jar ./src/META-INF/MANIFEST.MF


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

