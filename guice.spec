Name:      guice
Version:   2.0
Release:   5%{?dist}
Summary:   a lightweight dependency injection framework for Java 5 and above   
Group:         Development/Java
License:        GPL
URL:            http://code.google.com/p/google-guice/
Source0:        guice-2.0-src.jar
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: java-devel  
BuildRequires:  jpackage-utils
BuildRequires:  cglib
BuildRequires:  objectweb-asm

BuildArch: noarch
Requires:  java >= 1.5
Requires:  jpackage-utils
Requires: aopalliance
Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils

%description
Guice alleviates the need for factories and the use of new in your Java code. Think of Guice's @Inject as the new new. You will still need to write factories in some cases, but your code will not depend directly on them. Your code will be easier to change, unit test and reuse in other contexts.
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
classpath=src/:$(build-classpath aopalliance cglib.jar objectweb-asm/asm-all)

javac -d classes -cp $classpath `find . -name *.java` 
javadoc -d javadoc -classpath src/:%{_javadir}/aopalliance.jar:%{_javadir}/cglib.jar:%{_javadir}/objectweb-asm/asm-all.jar  $(for JAVA in `find src/ -name *.java` ; do  dirname $JAVA ; done | sort -u  | sed -e 's!src.!!'  -e 's!/!.!g'  )
find classes -name *.class | sed -e  's!classes/!!g' -e 's!^! -C classes !'  | xargs jar cf  %{name}-%{version}.jar

%install
#rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
install -m 755 -d $RPM_BUILD_ROOT%{_javadir}
install -m 755 %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -s %{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -m 755 -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp javadoc/*  $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%add_to_maven_depmap com.google.guice %{name} %{version} JPP %{name}
%add_to_maven_depmap com.google.inject %{name} %{version} JPP %{name}

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

