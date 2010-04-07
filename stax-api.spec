Name:      stax-api
Version:   1.0.1
Release:        1%{?dist}
Summary:       methods for iterative, event-based processing of XML documents. 

Group:         Development/Java
License:        GPL
URL:            http://dist.codehaus.org/stax/distributions/
Source0:        stax-src-1.2.0.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: ant
BuildRequires: java-devel  
BuildRequires:  jpackage-utils
BuildArch: noarch
Requires:  java >= specific_version
Requires:  jpackage-utils

%description
The StAX API exposes methods for iterative, event-based processing of XML documents. XML documents are treated as a filtered series of events, and infoset states can be stored in a procedural fashion. Moreover, unlike SAX, the StAX API is bidirectional, enabling both reading and writing of XML documents. 

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Documentation
Requires:       %{name}-%{version}-%{release}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -cT
jar -xf %{SOURCE0}

%build
ant all javadoc


%install
#rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
install -m 755 -d $RPM_BUILD_ROOT%{_javadir}
install -m 755    build/stax-api-%{version}.jar  $RPM_BUILD_ROOT%{_javadir} 
install -m 755 -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp build/javadoc/*  $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%add_to_maven_depmap org.apache.maven %{name} %{version} JPP %{name}

%clean
rm -rf $RPM_BUILD_ROOT


%post
%update_maven_depmap

%postun
%update_maven_depmap


%files
%defattr(-,root,root,-)
%{_javadir}/stax-api-%{version}.jar
/etc/maven/fragments/%{name}
%doc
%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}


%changelog
* Sun Apr 03 2010 Adam Young ayoung@redhat.com
- Specfile Created by pom2rpm by Adam Young ayoung@redhat.com 

