%global ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname buildr
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: A build system that doesn't suck
Name: rubygem-%{gemname}
Version: 1.3.5
Release: 4%{?dist}
Group: Development/Languages
License: ASL 2.0
URL: http://buildr.apache.org/
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Patch0:   buildr-buildpath.patch
Patch1:   buildr-fixversions.patch
Requires: ruby(abi) = 1.8
Requires: rubygems
Requires: rubygem(rake) >= 0.8.7
Requires: rubygem(builder) >= 2.1.2
Requires: rubygem(net-ssh) >= 2.0.15
Requires: rubygem(net-sftp) >= 2.0.2
Requires: rubygem(rubyzip) >= 0.9.1
Requires: rubygem(highline) >= 1.5.1
Requires: rubygem(rubyforge) >= 1.0.5
Requires: rubygem(hoe) >= 2.3.3
Requires: rubygem(rjb) >= 1.1.9
Requires: rubygem(Antwrap) >= 0.7.0
Requires: rubygem(rspec) >= 1.2.8
Requires: rubygem(xml-simple) >= 1.0.12
Requires: rubygem(archive-tar-minitar) >= 0.5.2
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Apache Buildr is a build system for Java-based applications, including support
for Scala, Groovy and a growing number of JVM languages and tools.  We wanted
something that's simple and intuitive to use, so we only need to tell it what
to do, and it takes care of the rest.  But also something we can easily extend
for those one-off tasks, with a language that's a joy to use.


%prep
%setup -q -c -T

%build
JAVA_HOME=/usr/lib/jvm/java gem install --local \
    --install-dir .%{gemdir} --force --rdoc %{SOURCE0}

echo $PWD
pushd ./%{geminstdir}
patch -p0 <  %{PATCH0}
patch -p0 <  %{PATCH1}
popd 

%install

mkdir -p %{buildroot}/%{_bindir}
cp -R  . %{buildroot}
mv %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x
pushd  %{buildroot}%{geminstdir}
#patch -p0 <  %{PATCH0}
#patch -p0 <  %{PATCH1}
popd


mkdir -p %{buildroot}/usr/share/doc/%{gemdir}-%{version}
for DOC in LICENSE CHANGELOG README.rdoc NOTICE 
    do mv  %{buildroot}%{geminstdir}/$DOC %{buildroot}/usr/share/doc/%{gemdir}-%{version} 
done	

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/buildr
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc /usr/share/doc/%{gemdir}-%{version}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Mon May 10 2010 Adam Young <ayoung@redhat.com> 
- Added a patch to Fix version issues introduced by ruby gems 1.3.6

* Fri May 07 2010 Adam Young <ayoung@redhat.com> 
- Added in a patch to allow us extend the build wrt maven repository.
- Changed %define to %global
- Moved doc files out of the main tree.
- Removed buildroot boilerplate that now is a default part of rpmbuild

* Thu Apr 01 2010 Adam Young <ayoung@redhat.com> - 1.3.5-1
- Initial package
