# Generated from cucumber-0.6.4.gem by gem2rpm -*- rpm-spec -*-
%global ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname cucumber
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Behaviour Driven Development with elegance and joy
Name: rubygem-%{gemname}
Version: 0.6.4
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://cukes.info
Source0: http://gems.rubyforge.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
Requires: rubygem(term-ansicolor) >= 1.0.4
Requires: rubygem(treetop) >= 1.4.2
Requires: rubygem(polyglot) >= 0.2.9
Requires: rubygem(builder) >= 2.1.2
Requires: rubygem(diff-lcs) >= 1.1.2
Requires: rubygem(json_pure) >= 1.2.0
Requires: rubygem(nokogiri) >= 1.4.1
Requires: rubygem(prawn) = 0.6.3
Requires: rubygem(prawn-format) = 0.2.3
Requires: rubygem(htmlentities) >= 4.2.0
Requires: rubygem(rspec) >= 1.3.0
Requires: rubygem(syntax) >= 1.0.0
Requires: rubygem(spork) >= 0.7.5
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
A BDD tool written in Ruby


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
%{_bindir}/cucumber
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README.rdoc
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Tue Apr 06 2010 Adam Young <ayoung@ayoung.boston.devel.redhat.com> - 0.6.4-1
- Initial package
