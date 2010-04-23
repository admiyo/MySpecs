# Generated from ruby-debug-0.10.3.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname ruby-debug
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Command line interface (CLI) for ruby-debug-base
Name: rubygem-%{gemname}
Version: 0.10.3
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://rubyforge.org/projects/ruby-debug/
Source0: http://gems.rubyforge.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
Requires: rubygem(columnize) >= 0.1
Requires: rubygem(ruby-debug-base) >= 0.10.3
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
A generic command line interface for ruby-debug.


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
find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/rdebug
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Fri Apr 23 2010 Adam Young <ayoung@redhat.com> - 0.10.3-1
- Initial package
