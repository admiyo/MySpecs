Name:      bcpg-jdk16
Version:   1.44
Release:        3%{?dist}
Summary:       The Bouncy Castle Java API for handling the OpenPGP protocol. This jar contains the OpenPGP API for JDK 1.6. The APIs can be used in conjunction with a JCE/JCA provider such as the one provided with the Bouncy Castle Cryptography APIs. 

Group:         Development/Java
License:        Bouncy Castle Licence
URL:            http://www.bouncycastle.org/java.html
Source0:        %{name}-%{version}-sources.jar
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch


BuildRequires: java-devel  
BuildRequires:  jpackage-utils
BuildRequires: bcprov-jdk16 = 1.44

Requires:  java >= 1.5
Requires:  jpackage-utils
Requires: bcprov-jdk16 = 1.44
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
classpath=src/:$(build-classpath bcprov-jdk16)
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

%add_to_maven_depmap org.bouncycastle %{name} %{version} JPP %{name}

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

