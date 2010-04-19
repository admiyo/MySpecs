# Copyright (c) 2000-2005, JPackage Project
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

%define _with_gcj_support 1
%define _without_maven 1
%define gcj_support %{?_with_gcj_support:1}%{!?_with_gcj_support:%{?_without_gcj_support:0}%{!?_without_gcj_support:%{?_gcj_support:%{_gcj_support}}%{!?_gcj_support:0}}}

# If you don't want to build with maven, and use straight ant instead,
# give rpmbuild option '--without maven'

%define with_maven %{!?_without_maven:1}%{?_without_maven:0}
%define without_maven %{?_without_maven:1}%{!?_without_maven:0}

%define base_name	collections
%define short_name	commons-%{base_name}
%define section		free

Name:		jakarta-%{short_name}
Version:	3.2.1
Release:	5%{?dist}
Epoch:		0
Summary:	Provides new interfaces, implementations and utilities for Java Collections
License:	ASL 2.0
Group:		Development/Libraries/Java
Source0:	http://www.apache.org/dist/jakarta/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Source1:	pom-maven2jpp-depcat.xsl
Source2:	pom-maven2jpp-newdepmap.xsl
Source3:	pom-maven2jpp-mapdeps.xsl
Source4:	commons-collections-3.2-jpp-depmap.xml
Source5:	commons-build.tar.gz
Source6:	collections-tomcat5-build.xml

Patch0:         %{name}-javadoc-nonet.patch
Patch1:         commons-collections-3.2-project_xml.patch
Patch4:         commons-collections-3.2-build_xml.patch

Url:            http://jakarta.apache.org/commons/%{base_name}/
BuildRequires:	ant
BuildRequires:	ant-junit
BuildRequires:	jpackage-utils >= 0:1.6
BuildRequires:	xml-commons-apis >= 1.3
%if %{with_maven}
BuildRequires:	maven >= 0:1.1
BuildRequires:	maven-plugins-base
BuildRequires:	maven-plugin-test
BuildRequires:	maven-plugin-xdoc
BuildRequires:	maven-plugin-license
BuildRequires:	maven-plugin-changes
BuildRequires:	maven-plugin-jdepend
BuildRequires:	maven-plugin-jdiff
BuildRequires:	maven-plugin-jxr
BuildRequires:	maven-plugin-tasklist
BuildRequires:	maven-plugin-developer-activity
BuildRequires:	maven-plugin-file-activity
BuildRequires:	saxon
BuildRequires:	saxon-scripts
%endif

%if ! %{gcj_support}
BuildArch:	noarch
%endif
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Provides:	%{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:	%{short_name} < %{epoch}:%{version}-%{release}

%if %{gcj_support}
BuildRequires:		java-gcj-compat-devel
Requires(post):		java-gcj-compat
Requires(postun):	java-gcj-compat
%endif

Requires:       jpackage-utils

Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils


%description
The introduction of the Collections API by Sun in JDK 1.2 has been a
boon to quick and effective Java programming. Ready access to powerful
data structures has accelerated development by reducing the need for
custom container classes around each core object. Most Java2 APIs are
significantly easier to use because of the Collections API.
However, there are certain holes left unfilled by Sun's
implementations, and the Jakarta-Commons Collections Component strives
to fulfill them. Among the features of this package are:
- special-purpose implementations of Lists and Maps for fast access
- adapter classes from Java1-style containers (arrays, enumerations) to
Java2-style collections.
- methods to test or create typical set-theory properties of collections
such as union, intersection, and closure.

%package testframework
Summary:	Testframework for %{name}
Group:		Development/Testing
Requires:	%{name} = %{epoch}:%{version}-%{release}

%if %{gcj_support}
BuildRequires:		java-gcj-compat-devel
Requires(post):		java-gcj-compat
Requires(postun):	java-gcj-compat
%endif

%description testframework
%{summary}.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Documentation

%description javadoc
%{summary}.

%package tomcat5
Summary:	Jakarta Commons Collection dependency for Tomcat5
Group:		Development/Libraries/Java

%if %{gcj_support}
BuildRequires:		java-gcj-compat-devel
Requires(post):		java-gcj-compat
Requires(postun):	java-gcj-compat
%endif

%description tomcat5
A package that is specifically designed to fulfill to a Tomcat5 dependency.

%package testframework-javadoc
Summary:	Javadoc for %{name}-testframework
Group:		Development/Documentation

%description testframework-javadoc
%{summary}.

%if %{with_maven}
%package manual
Summary:	Documents for %{name}
Group:		Development/Documentation

%description manual
%{summary}.
%endif

%prep
cat <<EOT

                If you dont want to build with maven,
                give rpmbuild option '--without maven'

EOT

%setup -q -n %{short_name}-%{version}-src
gzip -dc %{SOURCE5} | tar xf -
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

%patch0 -p1
%patch1 -b .sav
# Avoid fail on error for GCJ. See FIXME below.
%if %{gcj_support}
%patch4 -b .sav
%endif
cp %{SOURCE6} .

# Fix file eof
%{__sed} -i 's/\r//' LICENSE.txt
%{__sed} -i 's/\r//' PROPOSAL.html
%{__sed} -i 's/\r//' RELEASE-NOTES.html
%{__sed} -i 's/\r//' README.txt
%{__sed} -i 's/\r//' NOTICE.txt

%build
%if %{with_maven}
export DEPCAT=$(pwd)/commons-collections-3.2-depcat.new.xml
echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    /usr/bin/saxon project.xml %{SOURCE1} >> $DEPCAT
    popd
done
echo >> $DEPCAT
echo '</depset>' >> $DEPCAT
/usr/bin/saxon $DEPCAT %{SOURCE2} > commons-collections-3.2-depmap.new.xml

for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    /usr/bin/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done

export MAVEN_HOME_LOCAL=$(pwd)/.maven

#        -Dmaven.test.failure.ignore=true \
maven \
        -Dmaven.repo.remote=file:/usr/share/maven/repository \
        -Dmaven.home.local=${MAVEN_HOME_LOCAL} \
        jar:jar javadoc:generate xdoc:transform
ant tf.javadoc
%else
#FIXME Enabling tests with gcj causes memory leaks!
# See http://gcc.gnu.org/bugzilla/show_bug.cgi?id=28423
%if %{gcj_support}
ant -Djava.io.tmpdir=. jar javadoc tf.validate tf.jar dist.bin dist.src tf.javadoc
%else
ant -Djava.io.tmpdir=. test dist tf.javadoc
%endif
%endif

# commons-collections-tomcat5
ant -f collections-tomcat5-build.xml

%install
rm -rf $RPM_BUILD_ROOT
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
%if %{with_maven}
install -m 644 target/%{short_name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 target/%{short_name}-testframework-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-testframework-%{version}.jar
%else
install -m 644 build/%{short_name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 build/%{short_name}-testframework-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-testframework-%{version}.jar
%endif

#tomcat5
install -m 644 collections-tomcat5/%{short_name}-tomcat5.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-tomcat5-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|jakarta-||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%if %{with_maven}
cp -pr target/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%else
cp -pr build/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%endif
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
rm -rf target/docs/apidocs

# testframework-javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-testframework-%{version}
cp -pr build/docs/testframework/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-testframework-%{version}
ln -s %{name}-testframework-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-testframework 

# manual
%if %{with_maven}
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr target/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif



%add_to_maven_depmap org.apache.commons.commons-collections %{name} %{version} JPP %{name}
%add_to_maven_depmap commons-collections commons-collections %{version} JPP %{name}


%clean
rm -rf $RPM_BUILD_ROOT

%post
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif
%update_maven_depmap


%postun
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif
%update_maven_depmap

%post testframework
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%postun testframework
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%post tomcat5
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%postun tomcat5 
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif


%files
%defattr(0644,root,root,0755)
%doc PROPOSAL.html README.txt LICENSE.txt RELEASE-NOTES.html NOTICE.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{short_name}-%{version}.jar
%{_javadir}/%{short_name}.jar

%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%endif

%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/jakarta-commons-collections-3.2.1.jar.*
%endif

%files testframework
%defattr(0644,root,root,0755)
%{_javadir}/%{name}-testframework-%{version}.jar
%{_javadir}/%{name}-testframework.jar
%{_javadir}/%{short_name}-testframework-%{version}.jar
%{_javadir}/%{short_name}-testframework.jar
%{_mavendepmapfragdir}


%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/jakarta-commons-collections-testframework-3.2.1.jar.*
%endif

%files tomcat5
%defattr(0644,root,root,0755)
%{_javadir}/*-tomcat5*.jar
%doc LICENSE.txt NOTICE.txt
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*-tomcat5*
%endif

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files testframework-javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-testframework-%{version}
%{_javadocdir}/%{name}-testframework

%if %{with_maven}
%files manual
%defattr(0644,root,root,0755)
%{_docdir}/%{name}-%{version}
%endif

%changelog
* Mon Apr 19 2010 Adam Young <ayoung@redhat.com>
- Added JPP Maven Repository Support

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Devrim GUNDUZ <devrim@commandprompt.com> - 0:3.2.1-1
- Updated to 3.2.1
- Updated patch #1 and #4
- Own %dir %{_libdir}/gcj/%{name}, per #473612.

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:3.2-2.3
- drop repotag

* Sun Mar 2 2008 Devrim GUNDUZ <devrim@commandprompt.com> - 0:3.2-2jpp.2
- Add missing sources, per #434059

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0:3.2-2jpp.1
- Autorebuild for GCC 4.3

* Sat Feb 9 2008 Devrim GUNDUZ <devrim@commandprompt.com> - 0:3.2-1jpp.1
- Updated to 3.2
- Removed patch2 and patch3
- Updated patch1 and patch4.
- Fix license

* Wed Apr 25 2007 Matt Wringe <mwringe@redhat.com> - 0:3.1-9jpp.2
- A couple of spec file cleanups for Fedora Review

* Mon Mar 12 2007 Matt Wringe <mwringe@redhat.com> - 0:3.1-9jpp.1
- Merge with jpp version
- Fix rpmlint issues

* Fri Feb 23 2007 Jason Corley <jason.corley@gmail.com> 0:3.1-9jpp
- update copyright to contain current year
- rebuild on RHEL4 to avoid broken jar repack script in FC6

* Fri Jan 26 2007 Matt Wringe <mwringe@redhat.com> - 0:3.1-8jpp
- Fix bug in collections-tomcat5-build.xml

* Fri Jan 19 2007 Matt Wringe <mwringe@redhat.com> - 0:3.1-7jpp
- Add tomcat5 subpackage
- Add versioning to provides and obsoletes
- Move rm -rf %%RPM_BUILD_ROOT from %%prep to %%install
- Add missing maven dependencies

* Fri Aug 04 2006 Vivek Lakshmanan <vivekl@redhat.com> - 0:3.1-6jpp.1
- Resync with JPP.

* Fri Aug 04 2006 Vivek Lakshmanan <vivekl@redhat.com> - 0:3.1-5jpp.3
- Partially adopt new naming convention.
- Add proper Requires(x) statements where appropriate.

* Sat Jul 22 2006 Jakub Jelinek <jakub@redhat.com> - 0:3.1-5jpp_2fc
- Rebuilt

* Thu Jul 20 2006 Vivek Lakshmanan <vivekl@redhat.com> - 0:3.1-5jpp-1fc
- Resync with latest JPP version.

* Thu Jul 20 2006 Vivek Lakshmanan <vivekl@redhat.com> - 0:3.1-4jpp-3fc
- Remove define statements for NVR.

* Tue Jul 18 2006 Vivek Lakshmanan <vivekl@redhat.com> - 0:3.1-4jpp-2fc
- Add bug # for bug forcing disabling of tests for GCJ.

* Mon Jul 17 2006 Vivek Lakshmanan <vivekl@redhat.com> - 0:3.1-4jpp-1fc
- Add conditional native compilation.
- Update commons-collections-3.1-project_xml.patch to exclude reference
  to maven-plugin-changelog which requires netbeans-svc etc.
- Set test.failonerror to false and add patch for build.xml for ant builds
  with gcj to avoid stopping the build on test failures on GCJ.
- Merge with latest JPP version.

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0:3.1-2jpp_6fc
- rebuild

* Mon Mar  6 2006 Jeremy Katz <katzj@redhat.com> - 0:3.1-2jpp_5fc
- stop the scriptlet spew

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0:3.1-2jpp_4fc
- bump again for double-long bug on ppc(64)

* Wed Dec 21 2005 Jesse Keating <jkeating@redhat.com> 0:3.1-2jpp_3fc
- rebuilt again

* Tue Dec 13 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Jul 19 2005 Gary Benson <gbenson at redhat.com> - 0:3.1-2jpp_2fc
- Build on ia64, ppc64, s390 and s390x.
- Switch to aot-compile-rpm.

* Tue Jun 14 2005 Gary Benson <gbenson at redhat.com> - 0:3.1-2jpp_1fc
- Remove jarfiles from the tarball.

* Wed May 25 2005 Gary Benson <gbenson at redhat.com> - 0:3.1-2jpp
- Do not fetch stuff from sun.com during javadoc generation.
- Add build dependency on ant-junit.

* Wed May 25 2005 Gary Benson <gbenson@redhat.com> - 0:3.1-1jpp_5fc
- Rearrange how BC-compiled stuff is built and installed.

* Mon May 23 2005 Gary Benson <gbenson@redhat.com> - 0:3.1-1jpp_4fc
- Add alpha to the list of build architectures (#157522).
- Use absolute paths for rebuild-gcj-db.

* Thu May  5 2005 Gary Benson <gbenson@redhat.com> - 0:3.1-1jpp_3fc
- Add dependencies for %%post and %%postun scriptlets (#156901).

* Wed May  4 2005 Gary Benson <gbenson@redhat.com> - 0:3.1-1jpp_2fc
- BC-compile.
- Do not fetch stuff from sun.com during javadoc generation.

* Thu Jan 20 2005 Gary Benson <gbenson@redhat.com> - 0:3.1-1jpp_1fc
- Build into Fedora.

* Thu Oct 21 2004 Fernando Nasser <fnasser@redhat.com> - 0:3.1-1jpp_1rh
- Merge with upstream new version

* Fri Oct 1 2004 Andrew Overholt <overholt@redhat.com> 0:2.1-4jpp_6rh
- add coreutils BuildRequires

* Thu Sep 16 2004 Ralph Apel <r.apel at r-apel.de> - 0:3.1-1jpp
- Upgrade to 3.1

* Sun Aug 23 2004 Randy Watler <rwatler at finali.com> - 0:2.1.1-2jpp
- Rebuild with ant-1.6.2

* Fri Jul 2 2004 Aizaz Ahmed <aahmed@redhat.com> 0:2.1-4jpp_5rh
- Added trigger to restore symlinks that are removed if ugrading
  from a commons-collections rhug package

* Sun Jun 27 2004 Kaj J. Niemi <kajtzu@fi.basen.net> 0:2.1.1-1jpp
- Update to 2.1.1

* Fri Apr  2 2004 Frank Ch. Eigler <fche@redhat.com> 0:2.1-4jpp_4rh
- more of the same, for version-suffixed .jar files

* Fri Mar 26 2004 Frank Ch. Eigler <fche@redhat.com> 0:2.1-4jpp_3rh
- add RHUG upgrade cleanup

* Fri Mar  5 2004 Frank Ch. Eigler <fche@redhat.com> 0:2.1-4jpp_2rh
- RH vacuuming part II

* Thu Mar  4 2004 Frank Ch. Eigler <fche@redhat.com> 0:2.1-4jpp_1rh
- RH vacuuming

* Fri May 09 2003 David Walluck <david@anti-microsoft.org> 0:2.1-4jpp
- update for JPackage 1.5

* Fri Mar 21 2003 Nicolas Mailhot <Nicolas.Mailhot (at) JPackage.org > 2.1-3jpp
- For jpackage-utils 1.5

* Thu Feb 27 2003 Henri Gomez <hgomez@users.sourceforge.net> 2.1-2jpp
- fix ASF license and add package tag

* Thu Oct 24 2002 Henri Gomez <hgomez@users.sourceforge.net> 2.1-1jpp
- 2.1
- remove build patch about Java APIS link

* Fri Jul 12 2002 Henri Gomez <hgomez@users.sourceforge.net> 2.0-4jpp
- override java.io.tmpdir to avoid build use /tmp

* Mon Jun 10 2002 Henri Gomez <hgomez@users.sourceforge.net> 2.0-3jpp
- use sed instead of bash 2.x extension in link area to make spec compatible 
  with distro using bash 1.1x

* Fri Jun 07 2002 Henri Gomez <hgomez@users.sourceforge.net> 2.0-2jpp
- added short names in %%{_javadir}, as does jakarta developpers 

* Mon May 06 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 2.0-1jpp 
- 2.0
- distribution tag
- group tag
- regenerated patch

* Sat Jan 19 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.0-5jpp
- renamed to %%{name}
- additional sources in individual archives
- versioned dir for javadoc
- section macro

* Fri Dec 7 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.0-4jpp
- javadoc into javadoc package

* Sat Nov 3 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.0-3jpp
- used original summary
- added missing license

* Sat Oct 13 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.0-2jpp
- first unified release
- used web page description
- s/jPackage/JPackage

* Mon Aug 27 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.0-1mdk
- first Mandrake release
