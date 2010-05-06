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

%global _with_gcj_support 1

%global gcj_support %{?_with_gcj_support:1}%{!?_with_gcj_support:%{?_without_gcj_support:0}%{!?_without_gcj_support:%{?_gcj_support:%{_gcj_support}}%{!?_gcj_support:0}}}

%global section free
%global cvs_version 2_7_0

Name:           xalan-j2
Version:        2.7.0
Release:        9.9%{?dist}
Epoch:          0
Summary:        Java XSLT processor
# samples/servlet/ApplyXSLTException.java is ASL 1.1
# src/org/apache/xpath/domapi/XPathStylesheetDOM3Exception.java is W3C
License:        ASL 1.1 and ASL 2.0 and W3C
#Source0:        http://www.apache.org/dist/xml/xalan-j/xalan-j_2_7_0-src.tar.gz
Source0:        xalan-j_%{cvs_version}-src-RHsemiCLEAN.tar.gz
Source1:        %{name}-serializer-MANIFEST.MF
Patch0:         %{name}-noxsltcdeps.patch
Patch1:         %{name}-manifest.patch
Patch2:         %{name}-crosslink.patch
#This patch uses xalan-j2-serializer.jar in the MANIFEST files instead of serializer
Patch3:		%{name}-src-MANIFEST-MF.patch
URL:            http://xalan.apache.org/
Group:          Text Processing/Markup/XML
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%if ! %{gcj_support}
BuildArch:      noarch
%endif
Provides:       jaxp_transform_impl
Requires:       jaxp_parser_impl
Requires:  jpackage-utils >= 0:1.6
Requires(post):		/usr/sbin/update-alternatives
Requires(preun):	/usr/sbin/update-alternatives
Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils

BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:	java-devel
BuildRequires:  ant
BuildRequires:  bcel
BuildRequires:	jlex
BuildRequires:	java_cup
BuildRequires:	regexp
BuildRequires:	sed
BuildRequires:	servletapi5
BuildRequires:  xerces-j2 >= 0:2.7.1
BuildRequires:  xml-commons-apis >= 0:1.3

%if %{gcj_support}
BuildRequires:		java-gcj-compat-devel
Requires(post):		java-gcj-compat
Requires(postun):	java-gcj-compat
%endif

%description
Xalan is an XSLT processor for transforming XML documents into HTML,
text, or other XML document types. It implements the W3C Recommendations
for XSL Transformations (XSLT) and the XML Path Language (XPath). It can
be used from the command line, in an applet or a servlet, or as a module
in other program.

%package        xsltc
Summary:        XSLT compiler
Group:          Text Processing/Markup/XML
Requires:       java_cup
Requires:	bcel
Requires:	jlex
Requires:	regexp
Requires:	jaxp_parser_impl

%if %{gcj_support}
BuildRequires:		java-gcj-compat-devel
Requires(post):		java-gcj-compat
Requires(postun):	java-gcj-compat
%endif

%description    xsltc
The XSLT Compiler is a Java-based tool for compiling XSLT stylesheets into
lightweight and portable Java byte codes called translets.

%package        manual
Summary:        Manual for %{name}
Group:          Text Processing/Markup/XML

%description    manual
Documentation for %{name}.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildRequires:  java-javadoc
# for /bin/rm and /bin/ln
Requires(post):		coreutils
Requires(postun):	coreutils

%description    javadoc
Javadoc for %{name}.

%package        demo
Summary:        Demo for %{name}
Group:          Text Processing/Markup/XML
Requires:       %{name} = %{epoch}:%{version}-%{release}, servlet
BuildRequires:  servlet

%if %{gcj_support}
BuildRequires:		java-gcj-compat-devel
Requires(post):		java-gcj-compat
Requires(postun):	java-gcj-compat
%endif

%description    demo
Demonstrations and samples for %{name}.

%prep
%setup -q -n xalan-j_%{cvs_version}
%patch0 -p0
%patch3 -p0
#%patch1 -p0
#%patch2 -p0
# Remove all binary libs, except ones needed to build docs and N/A elsewhere.
for j in $(find . -name "*.jar"); do
	mv $j $j.no
done
# FIXME who knows where the sources are? xalan-j1 ?
mv tools/xalan2jdoc.jar.no tools/xalan2jdoc.jar
mv tools/xalan2jtaglet.jar.no tools/xalan2jtaglet.jar

%build
if [ ! -e "$JAVA_HOME" ] ; then export JAVA_HOME="%{java_home}" ; fi
pushd lib
ln -sf $(build-classpath java_cup-runtime) runtime.jar
ln -sf $(build-classpath bcel) BCEL.jar
ln -sf $(build-classpath regexp) regexp.jar
ln -sf $(build-classpath xerces-j2) xercesImpl.jar
ln -sf $(build-classpath xml-commons-apis) xml-apis.jar
popd
pushd tools
ln -sf $(build-classpath java_cup) java_cup.jar
ln -sf $(build-classpath ant) ant.jar
ln -sf $(build-classpath jlex) JLex.jar
ln -sf $(build-classpath xml-stylebook) stylebook-1.0-b3_xalan-2.jar
popd
export CLASSPATH=$(build-classpath servletapi5)

ant \
  -Djava.awt.headless=true \
  -Dapi.j2se=%{_javadocdir}/java \
  -Dbuild.xalan-interpretive.jar=build/xalan-interpretive.jar \
  xalan-interpretive.jar\
  xsltc.unbundledjar \
  docs \
  xsltc.docs \
  javadocs \
  samples \
  servlet


%install
rm -rf $RPM_BUILD_ROOT

# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE1} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u build/serializer.jar META-INF/MANIFEST.MF

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 644 build/xalan-interpretive.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -p -m 644 build/xsltc.jar \
  $RPM_BUILD_ROOT%{_javadir}/xsltc-%{version}.jar
install -p -m 644 build/serializer.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-serializer-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
rm -rf build/docs/apidocs

# demo
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 build/xalansamples.jar \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}-samples.jar
install -p -m 644 build/xalanservlet.war \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}-servlet.war
cp -pr samples $RPM_BUILD_ROOT%{_datadir}/%{name}

# fix link between manual and javadoc
(cd build/docs; ln -sf %{_javadocdir}/%{name}-%{version} apidocs)

# jaxp_transform_impl ghost symlink
ln -s %{_sysconfdir}/alternatives \
  $RPM_BUILD_ROOT%{_javadir}/jaxp_transform_impl.jar


%if %{gcj_support}
%{_bindir}/aot-compile-rpm --exclude %{_datadir}/%{name}/%{name}-servlet.war
%endif

%add_to_maven_depmap xalan xalan %{version} JPP xalan-j2


%clean
rm -rf $RPM_BUILD_ROOT


%post
update-alternatives --install %{_javadir}/jaxp_transform_impl.jar \
  jaxp_transform_impl %{_javadir}/%{name}.jar 30

%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%update_maven_depmap

%if %{gcj_support}
%postun
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%update_maven_depmap

%preun
{
  [ $1 = 0 ] || exit 0
  update-alternatives --remove jaxp_transform_impl %{_javadir}/%{name}.jar
} >/dev/null 2>&1 || :

#%post xsltc
#update-alternatives --install %{_javadir}/jaxp_transform_impl.jar \
#  jaxp_transform_impl %{_javadir}/xsltc.jar 10

#%preun xsltc
#{
#  [ $1 = 0 ] || exit 0
#  update-alternatives --remove jaxp_transform_impl %{_javadir}/xsltc.jar
#} >/dev/null 2>&1 || :

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{name}
fi

%post xsltc
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%postun xsltc
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%post demo
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%postun demo
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%files
%defattr(0644,root,root,0755)
%doc KEYS licenses/xalan.LICENSE.txt licenses/xalan.NOTICE.txt licenses/serializer.LICENSE.txt licenses/serializer.NOTICE.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-serializer-%{version}.jar
%{_javadir}/%{name}-serializer.jar
%ghost %{_javadir}/jaxp_transform_impl.jar

%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-serializer-%{version}.jar.*
%endif


%files xsltc
%defattr(0644,root,root,0755)
%{_javadir}/xsltc-%{version}.jar
%{_javadir}/xsltc.jar
#%ghost %{_javadir}/jaxp_transform_impl.jar
%{_mavendepmapfragdir}

%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/xsltc-%{version}.jar.*
%endif

%files manual
%defattr(0644,root,root,0755)
%doc build/docs/*

%files javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%files demo
%defattr(0644,root,root,0755)
%{_datadir}/%{name}

%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-samples.jar.*
%endif

%changelog

* Mon Apr 19 2010 Adam Young <ayoung@redhat.com>
- Added JPP Maven Repository Fragment

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.7.0-9.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.7.0-8.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 3 2009 Alexander Kurtakov <akurtako@redhat.com> 0:2.7.0-7.5
- Add osgi manifest.

* Sat Sep  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0:2.7.0-7.4
- fix license tag

* Thu Jul 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:2.7.0-7.3
- drop repotag
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0:2.7.0-7jpp.2
- Autorebuild for GCC 4.3

* Fri Apr 20 2007 Vivek Lakshmanan <vivekl@redhat.com> - 0:2.7.0-6jpp.2.fc7
- Rebuild to fix incomplete .db/so files due to broken aot-compile-rpm

* Fri Aug 18 2006 Vivek Lakshmanan <vivekl@redhat.com> - 0:2.7.0-6jpp.1
- Resync with latest from JPP.

* Fri Aug 11 2006 Vivek Lakshmanan <vivekl@redhat.com> - 0:2.7.0-5jpp.3
- Rebuild.

* Thu Aug 10 2006 Vivek Lakshmanan <vivekl@redhat.com> - 0:2.7.0-5jpp.2
- Rebuild.

* Thu Aug 10 2006 Vivek Lakshmanan <vivekl@redhat.com> - 0:2.7.0-5jpp.1
- Resync with latest from JPP.
- Partially adopt new naming convention (.1 suffix).
- Use ln and rm explicitly instead of core-utils in Requires(x).

* Thu Aug 10 2006 Karsten Hopp <karsten@redhat.de> 2.7.0-4jpp_5fc
- Requires(post):     coreutils

* Wed Jul 26 2006 Vivek Lakshmanan <vivekl@redhat.com> - 0:2.7.0-4jpp_4fc
- Extend patch to cover all applicable MANIFEST files in src directory.

* Wed Jul 26 2006 Vivek Lakshmanan <vivekl@redhat.com> - 0:2.7.0-4jpp_3fc
- Apply patch to replace serializer.jar in MANIFEST file with 
  xalan-j2-serializer.jar.

* Sat Jul 22 2006 Jakub Jelinek <jakub@redhat.com> - 0:2.7.0-4jpp_2fc
- Rebuilt

* Fri Jul 21 2006 Vivek Lakshmanan <vivekl@redhat.com> - 0:2.7.0-4jpp_1fc
- Resync with latest JPP version.

* Wed Jul 19 2006 Vivek Lakshmanan <vivekl@redhat.com> - 0:2.7.0-3jpp_1fc
- Merge with latest version from jpp.
- Undo ExcludeArch since eclipse available for all arch-es.
- Remove jars from sources for new upstream version.
- Purge unused patches from previous release.
- Conditional native compilation with GCJ.
- Use NVR macros wherever possible.

* Wed Mar  8 2006 Rafael Schloming <rafaels@redhat.com> - 0:2.6.0-3jpp_10fc
- excluded s390[x] and ppc64 due to eclipse

* Mon Mar  6 2006 Jeremy Katz <katzj@redhat.com> - 0:2.6.0-3jpp_9fc
- stop scriptlet spew

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0:2.6.0-3jpp_8fc
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0:2.6.0-3jpp_7fc
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Dec 21 2005 Jesse Keating <jkeating@redhat.com> 0:2.6.0-3jpp_6fc
- rebuild again

* Tue Dec 13 2005 Jesse Keating <jkeating@redhat.com> 0:2.6.0-3jpp_5fc.3
- patch to not use target= in build.xml

* Tue Dec 13 2005 Jesse Keating <jkeating@redhat.com> 0:2.6.0-3jpp_5fc.1
- rebuild again with gcc-4.1

* Fri Dec 09 2005 Warren Togami <wtogami@redhat.com> 0:2.6.0-3jpp_5fc
- rebuild with gcc-4.1

* Tue Nov  1 2005 Archit Shah <ashah at redhat.com> 0:2.6.0-3jpp_4fc
- Exclude war which blocks aot compilation of main jar (#171005).

* Tue Jul 19 2005 Gary Benson <gbenson at redhat.com> 0:2.6.0-3jpp_3fc
- Build on ia64, ppc64, s390 and s390x.
- Switch to aot-compile-rpm (also BC-compiles xsltc and samples).

* Tue Jun 28 2005 Gary Benson <gbenson at redhat.com> 0:2.6.0-3jpp_2fc
- Remove a tarball from the tarball too.
- Fix demo subpackage's dependencies.

* Wed Jun 15 2005 Gary Benson <gbenson at redhat.com> 0:2.6.0-3jpp_1fc
- Remove jarfiles from the tarball.

* Fri May 27 2005 Gary Benson <gbenson at redhat.com> 0:2.6.0-3jpp
- Add NOTICE file as per Apache License version 2.0.
- Build with servletapi5.

* Fri May 27 2005 Gary Benson <gbenson@redhat.com> 0:2.6.0-2jpp_3fc
- Remove now-unnecessary workaround for #130162.
- Rearrange how BC-compiled stuff is built and installed.

* Tue May 24 2005 Gary Benson <gbenson@redhat.com> 0:2.6.0-2jpp_2fc
- Add DOM3 stubs to classes that need them (#152255).
- BC-compile the main jarfile.

* Fri Apr  1 2005 Gary Benson <gbenson@redhat.com>
- Add NOTICE file as per Apache License version 2.0.

* Wed Jan 12 2005 Gary Benson <gbenson@redhat.com> 0:2.6.0-2jpp_1fc
- Sync with RHAPS.

* Mon Nov 15 2004 Fernando Nasser <fnasser@redhat.com> 0:2.6.0-2jpp_1rh
- Merge with latest community release

* Thu Nov  4 2004 Gary Benson <gbenson@redhat.com> 0:2.6.0-1jpp_2fc
- Build into Fedora.

* Thu Aug 26 2004 Ralph Apel <r.ape at r-apel.de> 0:2.6.0-2jpp
- Build with ant-1.6.2
- Try with -Djava.awt.headless=true 

* Mon Jul 26 2004 Fernando Nasser <fnasser@redhat.com> 0:2.6.0-1jpp_1rh
- Merge with latest community version

* Fri Mar 26 2004 Frank Ch. Eigler <fche@redhat.com> 0:2.5.2-1jpp_2rh
- add RHUG upgrade cleanup

* Tue Mar 23 2004 Kaj J. Niemi <kajtzu@fi.basen.net> 0:2.6.0-1jpp
- Updated to 2.6.0 
- Patches supplied by <aleksander.adamowski@altkom.pl>

* Thu Mar  4 2004 Frank Ch. Eigler <fche@redhat.com> - 0:2.5.2-1jpp_1rh
- RH vacuuming

* Sat Nov 15 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.5.2-1jpp
- Update to 2.5.2.
- Re-enable javadocs, new style versionless symlink handling, crosslink
  with local J2SE javadocs.
- Spec cleanups.

* Sat Jun  7 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.5.1-1jpp
- Update to 2.5.1.
- Fix jpackage-utils version in BuildRequires, add xerces-j2.
- Non-versioned javadoc symlinking.
- Add one missing epoch.
- Clean up manifests from Class-Path's and other stuff we don't include.
- xsltc no longer provides a jaxp_transform_impl because of huge classpath
  and general unsuitablity for production-use, system-installed transformer.
- Own (ghost) %%{_javadir}/jaxp_transform_impl.jar.
- Remove alternatives in preun instead of postun.
- Disable javadoc subpackage for now:
  <http://issues.apache.org/bugzilla/show_bug.cgi?id=20572>

* Thu Mar 27 2003 Nicolas Mailhot <Nicolas.Mailhot@One2team.com> 0:2.5.0.d1-1jpp
- For jpackage-utils 1.5

* Wed Jan 22 2003 Ville Skyttä <ville.skytta at iki.fi> - 2.4.1-2jpp
- bsf -> oldbsf.
- Use non-versioned jar in alternative, don't remove it on upgrade.
- Remove hardcoded packager tag.

* Mon Nov 04 2002 Henri Gomez <hgomez@users.sourceforge.net> 2.4.1-1jpp
- 2.4.1

* Tue Sep 10 2002 Ville Skyttä <ville.skytta at iki.fi> 2.4.0-1jpp
- 2.4.0.

* Thu Aug 22 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 2.4-0.D1.3jpp
- corrected case for Group tag
- fixed servlet classpath

* Tue Aug 20 2002 Ville Skyttä <ville.skytta at iki.fi> 2.4-0.D1.2jpp
- Remove xerces-j1 runtime dependency.
- Add bcel, jlex, regexp to xsltc runtime requirements:
  <http://xml.apache.org/xalan-j/xsltc_usage.html>
- Build with -Dbuild.compiler=modern (IBM 1.3.1) to avoid stylebook errors.
- XSLTC now provides jaxp_transform_impl too.
- Earlier changes by Henri, from unreleased 2.4-D1.1jpp:
    Mon Jul 15 2002 Henri Gomez <hgomez@users.sourceforge.net> 2.4-D1.1jpp
  - 2.4D1
  - use the jlex 1.2.5-5jpp (patched by Xalan/XSLTC team) rpm
  - use the stylebook-1.0-b3_xalan-2.jar included in source file till it will
    be packaged in jpackage
  - use jaxp_parser_impl (possibly xerces-j2) instead of xerces-j1 for docs
    generation, since it's tuned for stylebook-1.0-b3_xalan-2.jar
  - build and provide xsltc in a separate rpm

* Mon Jul 01 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 2.3.1-2jpp 
- provides jaxp_transform_impl
- requires jaxp_parser_impl
- stylebook already requires xml-commons-apis
- jaxp_parser_impl already requires xml-commons-apis
- use sed instead of bash 2.x extension in link area to make spec compatible with distro using bash 1.1x

* Wed Jun 26 2002 Henri Gomez <hgomez@users.sourceforge.net> 2.3.1-2jpp
- fix built classpath (bsf, bcel are existing jpackage rpms),
- add buildrequires for javacup and JLex

* Wed May 08 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 2.3.1-1jpp 
- 2.3.1
- vendor, distribution, group tags

* Mon Mar 18 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 2.3.0-2jpp 
- generic servlet support

* Wed Feb 20 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 2.3.0-1jpp 
- 2.3.0
- no more compat jar

* Sun Jan 27 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 2.2.0-2jpp 
- adaptation to new stylebook1.0b3 package
- used source tarball
- section macro

* Fri Jan 18 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 2.2.0-1jpp
- 2.2.0 final
- versioned dir for javadoc
- no dependencies for manual and javadoc packages
- stricter dependency for compat and demo packages
- fixed package confusion
- adaptation for new servlet3 package
- requires xerces-j1 instead of jaxp_parser
- xml-apis jar now in required xml-commons-apis external package

* Wed Dec 5 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 2.2.D14-1jpp
- 2.2.D14
- javadoc into javadoc package
- compat.jar into compat package
- compat javadoc into compat-javadoc package

* Wed Nov 21 2001 Christian Zoffoli <czoffoli@littlepenguin.org> 2.2.D13-2jpp
- changed extension to jpp
- prefixed xml-apis

* Tue Nov 20 2001 Christian Zoffoli <czoffoli@littlepenguin.org> 2.2.D13-1jpp
- 2.2.D13
- removed packager tag

* Sat Oct 6 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 2.2.D11-1jpp
- 2.2.D11

* Sun Sep 30 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 2.2.D10-2jpp
- first unified release
- s/jPackage/JPackage

* Fri Sep 14 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 2.2.D10-1mdk
- cvs references
- splitted demo package
- moved demo files to %{_datadir}/%{name}
- only manual package requires stylebook-1.0b3
- only demo package requires servletapi3

* Wed Aug 22 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 2.2.D9-1mdk
- 2.2.9
- used new source packaging policy
- added samples data

* Wed Aug 08 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 2.2.D6-1mdk
- first Mandrake release
