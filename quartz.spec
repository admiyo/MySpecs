# Copyright (c) 2000-2008, JPackage Project
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_with bootstrap
%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/quartz/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define section free

Name:           quartz
Epoch:          0
Version:        1.5.2
Release:	7%{?dist}
Summary:        Quartz Enterprise Job Scheduler
License:        ASL 2.0
URL:            http://www.opensymphony.com/quartz/
Group:          Development/Libraries/Java
Source0:        %{name}-%{version}.zip
Source1:        quartz-component-info.xml
Patch0:         %{name}-%{version}-build_xml.patch
BuildRequires:  jpackage-utils >= 0:1.5
BuildRequires:  ant >= 0:1.6
BuildRequires:  junit
BuildRequires:  java >= 0:1.4
BuildRequires:  ejb_2_1_api
BuildRequires:  jaf
BuildRequires:  jakarta-commons-beanutils
BuildRequires:  jakarta-commons-collections
BuildRequires:  jakarta-commons-validator
BuildRequires:  jakarta-commons-dbcp
BuildRequires:  jakarta-commons-digester
BuildRequires:  jakarta-commons-logging
BuildRequires:  jakarta-commons-pool
%if %with bootstrap
BuildRequires:  jboss4-server
BuildRequires:  jboss4-jmx
BuildRequires:  jboss4-common
BuildRequires:  jboss4-system
%else
BuildRequires:  jbossas
%endif
BuildRequires:  javamail
BuildRequires:  jta
BuildRequires:  log4j
BuildRequires:  mx4j
BuildRequires:  servletapi5
Requires:  java >= 0:1.4
Requires:  jaf
Requires:  jakarta-commons-beanutils
Requires:  jakarta-commons-collections
Requires:  jakarta-commons-dbcp
Requires:  jakarta-commons-digester
Requires:  jakarta-commons-logging
Requires:  jakarta-commons-pool
#Optional:  javamail
Requires:  log4j
Requires:  servletapi5
Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Quartz is a job scheduling system that can be integrated with, or used 
along side virtually any J2EE or J2SE application. Quartz can be used 
to create simple or complex schedules for executing tens, hundreds, or 
even tens-of-thousands of jobs; jobs whose tasks are defined as standard 
Java components or EJBs. 

Note: If you want Quartz to be able to send e-mail then add javamail.jar to
your ClassPath.

%if %with repolib
%package repolib
Summary:         Artifacts to be uploaded to a repository library
Group:           Development/Libraries/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package demo
Summary:        Examples for %{name}
Group:          Development/Documentation
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description demo
Examples for %{name}.

%package manual
Summary:        Manual for %{name}
Group:          Development/Documentation

%description manual
Manual for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
find . -type f -name "*.jar" | xargs rm
perl -pi -e 's/\r$//g' docs/dbTables/*.sql docs/xml/job_scheduling_data_1_5.dtd
perl -pi -e 's/\r/\n/g' docs/dbTables/tables_db2.sql
# 
#sed -e 's+lib\.jboss-common\.jar=.*$+lib\.jboss-common\.jar=/usr/share/java/jboss4/jboss-common\.jar+' \
#        -e 's+lib\.jboss-jmx\.jar=.*$+lib\.jboss-jmx\.jar=/usr/share/java/jboss4/jboss-jmx\.jar+' \
#        -e 's+lib\.jboss-system\.jar=.*$+lib\.jboss-system\.jar=/usr/share/java/jboss4/jboss-system\.jar+' \
#        -e 's+lib\.jboss\.jar=.*$+lib\.jboss\.jar=/usr/share/java/jboss4/jboss\.jar+' \
#        build.properties > build.properties.mod
#cp build.properties.mod build.properties
#rm build.properties.mod
pushd lib
#ln -s $(find-jar oracle-jdbc-thin) classes12.zip
#ln -s $(find-jar servletapi5) servlet.jar
#ln -s $(find-jar commons-dbcp) commons-dbcp-1.1.jar
#ln -s $(find-jar jta) jta.jar 
#ln -s $(find-jar mx4j/mx4j-jmx) jmx.jar 
#ln -s $(find-jar ejb_2_1_api) ejb.jar 
#ln -s $(find-jar commons-beanutils) commons-beanutils.jar
#ln -s $(find-jar commons-digester) commons-digester.jar
#ln -s $(find-jar jdbc-stdext) jdbc2_0-stdext.jar 
#ln -s $(find-jar jaf) activation.jar 
#ln -s $(find-jar javamail) javamail.jar 
#ln -s $(find-jar commons-collections) commons-collections.jar
#ln -s $(find-jar commons-logging) commons-logging.jar 
#ln -s $(find-jar commons-pool) commons-pool-1.1.jar
#ln -s $(find-jar log4j) log4j.jar
#ln -s $(find-jar junit) junit.jar

#commons-beanutils.jar (1.7.0)
#- buildtime, runtime, optional
ln -s $(find-jar commons-beanutils) .
#commons-collections-3.1.jar (3.1)
#- runtime, required 
ln -s $(find-jar commons-collections) .
#commons-dbcp-1.2.1.jar (1.2.1)
#- runtime, optional
ln -s $(find-jar commons-dbcp) .
#commons-digester-1.7.jar (1.7)
#- buildtime, runtime, optional
ln -s $(find-jar commons-digester) .
#commons-logging.jar (1.0.4)
#- runtime, required
ln -s $(find-jar commons-logging) .
#commons-pool-1.2.jar (1.2)
#- runtime, optional
ln -s $(find-jar commons-pool) .
#jdbc2_0-stdext.jar
#- Standard JDBC APIs
#- runtime, required
ln -s $(find-jar jdbc-stdext) .
#ejb.jar (2.0)
#- Enterprise Java Beans API
#- buildtime, runtime, optional
ln -s $(find-jar ejb_2_1_api) .
#jta.jar
#- Standard JTA API
#- runtime, optional
ln -s $(find-jar jta) .
#servlet.jar (2.3)
#- Servlet API (2.3)
#- buildtime, runtime, optional
# XXX: can use 2.4 for build
ln -s $(find-jar servletapi5) .
#junit.jar (3.8.1)
#- JUnit test framework
#- buildtime
ln -s $(find-jar junit) .
#activation.jar (1.1)
#- Javax Activation framework
ln -s $(find-jar jaf) .
#mail.jar (1.3.3)
#- Javax Mail api
ln -s $(find-jar javamail) .
#log4j-1.2.11.jar (1.2.11)
#- Log4j Logging Framework 
#- runtime, optional
ln -s $(find-jar log4j) .
#commons-validator-1.1.4.jar (1.1.4)
#- Commons Validation Framework
#- runtime, optional
ln -s $(find-jar commons-validator) .

%if %with bootstrap
ln -s $(find-jar jboss4/jboss-common) .
ln -s $(find-jar jboss4/jboss-jmx) .
ln -s $(find-jar jboss4/jboss-system) .
ln -s $(find-jar jboss4/jboss) .
%else
ln -s $(build-classpath jbossas/jbossall-client) .
ln -s $(build-classpath jbossas/jboss-jmx) .
ln -s $(build-classpath jbossas/jboss-system) .
ln -s $(build-classpath jbossas/jboss) .
%endif
popd

%patch0 -b .sav
mkdir opensymphony
cp osbuild.xml opensymphony
cp EMPTY.MF opensymphony

%{__perl} -pi -e 's/\r$//g' readme.txt license.txt \
  `find . -name '*.sh' -o -name '*.css' -o -name '*.xml*' -o -name package-list`

find . -name '*.sh' | xargs %{__chmod} 0755

%build
export CLASSPATH=
export OPT_JAR_LIST=:
%{ant}

%install
rm -rf $RPM_BUILD_ROOT

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
cp -p build/%{name}-all-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-all-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
# FIXME: (dwalluck) This breaks -bi --short-circuit
rm -rf docs/api

# manual
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

# demo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr examples/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_datadir}/%{name}

%if %with repolib
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@VERSION@/%{version}-brew/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/quartz.jar $RPM_BUILD_ROOT%{repodirlib}/quartz.jar
%if 0
cp -p $RPM_BUILD_ROOT%{_javadir}/quartz-all.jar $RPM_BUILD_ROOT%{repodirlib}/quartz-all.jar
%endif
%endif

%add_to_maven_depmap org.quartz-scheduler %{name} %{version} JPP %{name}


%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_maven_depmap

%postun
%update_maven_depmap


%files
%defattr(0644,root,root,0755)
%doc readme.txt license.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}-all.jar
%{_javadir}/%{name}-all-%{version}.jar
%{_mavendepmapfragdir}

%files demo
%defattr(-,root,root,0755)
%{_datadir}/%{name}-%{version}
%{_datadir}/%{name}

%files manual
%defattr(0644,root,root,0755)
%{_docdir}/%{name}-%{version}

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%defattr(0644,root,root,0755)
%{_javadir}/repository.jboss.com
%endif

%changelog
* Mon Apr 19 2010 Adam Young <ayoung@redhat.com>
- Added JPP Maven repository support 

* Sat Jan 09 2010 Will Tatam <will.tatam@red61.com> 1.5.2-6
- Auto rebuild for JPackage 6 in centos5 mock

* Wed Jul 22 2009 David Walluck <dwalluck@redhat.com> 0:1.5.2-5
- update repolib for JBoss AS 5.1.0.GA

* Sat Jun 14 2008 David Walluck <dwalluck@redhat.com> 0:1.5.2-4
- build as non-bootstrap
- fix repolib

* Sat Jun 14 2008 David Walluck <dwalluck@redhat.com> 0:1.5.2-3.jpp5
- add non-bootstrap

* Thu May 29 2008 David Walluck <dwalluck@redhat.com> 0:1.5.2-2.jpp5
- fix file locations
- fix file eol
- fix .sh permissions
- fix License
- fix Requires for demo

* Mon Apr 21 2008 David Walluck <dwalluck@redhat.com> 0:1.5.2-1jpp.ep1.3
- servletapi4 was referenced but not in BuildRequires (use servletapi5)

* Tue Mar 13 2007 Fernando Nasser <fnasser@redhat.com> - 0:1.5.2-1jpp.ep1.2
- New repolib location

* Tue Mar 13 2007 Fernando Nasser <fnasser@redhat.com> - 0:1.5.2-1jpp.ep1.1
- Add note to description

* Mon Mar 05 2007 Fernando Nasser <fnasser@redhat.com> - 0:1.5.2-1jpp.el4ep1.3
- Mark javamail as optional

* Tue Feb 20 2007 Vivek Lakshmanan <vivekl@redhat.com> - 0:1.5.2-1jpp.el4ep1.2
- Add -brew suffix

* Sun Feb 18 2007 Vivek Lakshmanan <vivekl@redhat.com> - 0:1.5.2-1jpp.el4ep1.1
- Add repolib support
- Add missing BR on j-c-validator

* Tue Aug 01 2006 Fernando Nasser <fnasser@redhat.com> - 0:1.5.2-1jpp_1rh
- Merge with upstream

* Mon Jun 12 2006 Ralph Apel <r.apel at r-apel.de> - 0:1.5.2-1jpp
- Upgrade to 1.5.2

* Sun Mar 12 2006 Fernando Nasser <fnasser@redhat.com> - 0:1.4.5-2jpp_1rh
- First Red Hat build
- Disable JBoss cache

* Fri Mar 10 2006 Fernando Nasser <fnasser@redhat.com> - 0:1.4.5-2jpp
- First JPP 1.7 build
- Remove dependency on oracle

* Thu Sep 15 2005 Ralph Apel <r.apel at r-apel.de> - 0:1.4.5-1jpp
- Upgrade to 1.4.5

* Fri Oct 08 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.4.2-1jpp
- Upgrade to 1.4.2
- Relax some versioned dependencies

* Wed Aug 25 2004 Fernando Nasser <fnasser@redhat.com> - 0:1.2.3-2jpp
- Require ant > 1.6
- Update to servletapi5
- Rebuild with Ant 1.6.2

* Mon Jan 19 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.2.3-1jpp
- First JPackage build
