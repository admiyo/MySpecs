# Copyright (c) 2000-2009, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define	section		free


Name:		freemarker
Summary:	FreeMarker template engine
Url:		http://freemarker.sourceforge.net/
Version:	2.3.15
Release:	1%{?dist}
Epoch:		0
License:	BSD-style
Group:		Development/Libraries/Java
BuildArch:	noarch
Source0:	freemarker-2.3.15.tar.gz
Source1:	freemarker-2.3.15.pom
Patch0:		freemarker-2.3.15-JythonHashModel.patch
Patch1:		freemarker-2.3.15-BeansWrapper.patch
Patch2:		freemarker-2.3.15-NodeListModel.patch
Patch3:		freemarker-2.3.15-JdomNavigator.patch

BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:	java-devel >= 0:1.5.0
BuildRequires:	ant >= 0:1.6.5
BuildRequires:	ant-junit
BuildRequires:	ant-nodeps
BuildRequires:  emma
BuildRequires:  junit
BuildRequires:	javacc3
BuildRequires:	maven2
#BuildRequires:	servlet_2_3_api
BuildRequires:	jaxen >= 0:1.1
BuildRequires:	jython
BuildRequires:	excalibur-avalon-framework-api
BuildRequires:	excalibur-avalon-framework-impl
BuildRequires:	excalibur-avalon-logkit
BuildRequires:	dom4j
BuildRequires:	el_1_0_api
BuildRequires:	jdom
BuildRequires:	jsp_1_2_api
BuildRequires:	jsp_2_0_api
BuildRequires:	jsp_2_1_api
BuildRequires:	log4j
BuildRequires:	rhino
BuildRequires:	saxpath
BuildRequires:	servlet_2_5_api
BuildRequires:	struts
BuildRequires:	xerces-j2
BuildRequires:	xalan-j2
Requires:	java >= 0:1.5.0
Requires:	excalibur-avalon-framework-api
Requires:	excalibur-avalon-framework-impl
Requires:	excalibur-avalon-logkit
Requires:	servlet_api
Requires:	jaxen >= 0:1.1
Requires:	jython
Requires:	jdom
Requires:	dom4j
Requires:	el_1_0_api
Requires:	log4j
Requires:	rhino
Requires:	saxpath
Requires:	struts
Requires(post):    jpackage-utils >= 0:1.7.3
Requires(postun):  jpackage-utils >= 0:1.7.3

BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
FreeMarker is a "template engine"; a generic tool to 
generate text output (anything from HTML or RTF to 
autogenerated source code) based on templates.
FreeMarker is designed to be practical for the generation 
of HTML Web pages, particularly by servlet-based applications 
following the MVC (Model View Controller) pattern. 
Although FreeMarker has some programming capabilities, 
it is not a full-blown programming language like PHP. Instead, 
Java programs prepare the data to be displayed, and FreeMarker 
just generates textual pages that display the prepared data 
using templates. 
FreeMarker is not a Web application framework. It is suitable 
for a component in a Web application framework, but the 
FreeMarker engine itself knows nothing about HTTP or servlets. 


%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Documentation

%description javadoc
%{summary}.

%package manual
Summary:	Documents for %{name}
Group:		Development/Documentation

%description manual
%{summary}.

%prep
%setup -q -n %{name}-%{version}
chmod -R go=u-w *
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
#<available file="lib/README.txt"/>
touch lib/README.txt
#<available file="lib/ant.jar"/>
ln -sf $(build-classpath ant) lib
#<available file="lib/dom4j.jar"/>
ln -sf $(build-classpath dom4j) lib
#<available file="lib/emma.jar"/>
ln -sf $(build-classpath emma) lib
#<available file="lib/emma_ant.jar"/>
ln -sf $(build-classpath emma_ant) lib
#<available file="lib/javacc.jar"/>
ln -sf $(build-classpath javacc3) lib/javacc.jar
#<available file="lib/freemarker-bootstrap.jar"/>
mv lib/freemarker.jar.no lib/freemarker-bootstrap.jar
#<available file="lib/javarebel-sdk.jar"/>
ln -sf $(build-classpath maven2/empty-dep) lib/javarebel-sdk.jar
#<available file="lib/jaxen.jar"/>
ln -sf $(build-classpath jaxen) lib
#<available file="lib/jdom.jar"/>
ln -sf $(build-classpath jdom) lib
#<available file="lib/js.jar"/>
ln -sf $(build-classpath js) lib
#<available file="lib/junit.jar"/>
ln -sf $(build-classpath junit) lib
#<available file="lib/jython.jar"/>
ln -sf $(build-classpath jython) lib
#<available file="lib/log4j.jar"/>
ln -sf $(build-classpath log4j) lib
#<available file="lib/logkit.jar"/>
ln -sf $(build-classpath excalibur/avalon-logkit) lib/logkit.jar
#<available file="lib/rt122.jar"/>
#ln -sf $JAVA_HOME/jre/lib/rt.jar lib/rt122.jar
#<available file="lib/saxpath.jar"/>
ln -sf $(build-classpath saxpath) lib
#<available file="lib/servlet.jar"/>
ln -sf $(build-classpath servlet_2_5_api) lib/servlet.jar
#<available file="lib/struts.jar"/>
ln -sf $(build-classpath struts) lib
#<available file="lib/jsp-api-1.2.jar"/>
ln -sf $(build-classpath jsp_1_2_api) lib/jsp-api-1.2.jar
#<available file="lib/jsp-api-2.0.jar"/>
ln -sf $(build-classpath jsp_2_0_api) lib/jsp-api-2.0.jar
#<available file="lib/jsp-api-2.1.jar"/>
ln -sf $(build-classpath jsp_2_1_api) lib/jsp-api-2.1.jar
#<available file="lib/xalan.jar"/>
ln -sf $(build-classpath xalan-j2) lib/xalan.jar

%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3
rm src/freemarker/ext/beans/JavaRebelIntegration.java

%build
export JAVA_HOME=%{_jvmdir}/java
ln -sf $JAVA_HOME/jre/lib/rt.jar lib/rt122.jar
export OPT_JAR_LIST="ant/ant-junit junit ant/ant-nodeps javacc3"
export CLASSPATH=$(build-classpath \
el_1_0_api \
)
ant

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 lib/%{name}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
rm -rf docs/docs/api

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_maven_depmap

%postun
%update_maven_depmap

%files
%defattr(-,root,root)
%{_javadir}/*.jar
%{_docdir}/%{name}-%{version}/LICENSE.txt
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*

%files javadoc
%defattr(-,root,root)
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%defattr(-,root,root)
%{_docdir}/%{name}-%{version}

%changelog
* Mon Mar 23 2009 Ralph Apel <r.apel@r-apel.de> - 0:2.3.15-1.jpp5
- 2.3.15

* Mon Apr 24 2006 Fernando Nasser <fnasser@redhat.com> - 0:2.3.6-2jpp
- Use compat javacc3 package

* Thu Mar 30 2006 Ralph Apel <r.apel at r-apel.de> 0:2.3.6-1jpp
- Upgrade to 2.3.6
- Replace old avalon-framework, avalon-logkit with current excalibur-*

* Fri Mar 10 2006 Fernando Nasser <fnasser@redhat.com> 0:2.3-2jpp
- First JPP 1.7 build

* Fri Oct 08 2004 Ralph Apel <r.apel at r-apel.de> 0:2.3-1jpp
- First release
