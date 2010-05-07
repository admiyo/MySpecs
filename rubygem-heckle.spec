# Generated from heckle-1.4.3.gem by gem2rpm -*- rpm-spec -*-
%global ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname heckle
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Heckle is unit test sadism(tm) at it's core
Name: rubygem-%{gemname}
Version: 1.4.3
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://www.rubyforge.org/projects/seattlerb
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Patch0: heckle-local.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby(abi) = 1.8
Requires: rubygems
Requires: rubygem(ParseTree) >= 2.0.0
Requires: rubygem(ruby2ruby) >= 1.1.6
Requires: rubygem(ZenTest) >= 3.5.2
Requires: rubygem(hoe) >= 2.3.0
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Heckle is unit test sadism(tm) at it's core. Heckle is a mutation tester. It
modifies your code and runs your tests to make sure they fail. The idea is
that if code can be changed and your tests don't notice, either that code
isn't being covered or it doesn't do anything.
It's like hiring a white-hat hacker to try to break into your server and
making sure you detect it. You learn the most by trying to break things and
watching the outcome in an act of unit test sadism.


%prep


%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gemdir}/bin
pushd %{buildroot}%{geminstdir}/bin
patch -p0 <  %{PATCH0}
popd

mkdir -p %{buildroot}/usr/share/doc/%{gemdir}-%{version}
mv  %{buildroot}%{geminstdir}/History.txt %{buildroot}/usr/share/doc/%{gemdir}-%{version}
mv  %{buildroot}%{geminstdir}/Manifest.txt %{buildroot}/usr/share/doc/%{gemdir}-%{version}
mv  %{buildroot}%{geminstdir}/README.txt %{buildroot}/usr/share/doc/%{gemdir}-%{version}


find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/heckle
%{gemdir}/gems/%{gemname}-%{version}/
/usr/share/doc/%{gemdir}-%{version}
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc /usr/share/doc/%{gemdir}-%{version}

%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Wed Mar 31 2010 Adam Young <ayoung@ayoung.boston.devel.redhat.com> - 1.4.3-1
- Initial package
