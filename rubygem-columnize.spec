# Generated from columnize-0.3.1.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname columnize
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Read file with caching
Name: rubygem-%{gemname}
Version: 0.3.1
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://rubyforge.org/projects/rocky-hacks/columnize
Source0: http://gems.rubyforge.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Return a list of strings as a set of arranged in columns.
For example, for a line width of 4 characters (arranged vertically):
['1', '2,', '3', '4'] => '1  3
2  4
'
or arranged horizontally:
['1', '2,', '3', '4'] => '1  2
3  4
'
Each column is only as wide as necessary.  By default, columns are
separated by two spaces - one was not legible enough. Set "colsep"
to adjust the string separate columns. Set `displaywidth' to set
the line width.
Normally, consecutive items go down from the top to bottom from
the left-most column to the right-most. If +arrange_vertical+ is
set false, consecutive items will go across, left to right, top to
bottom.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README
%doc %{geminstdir}/lib/columnize.rb
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Fri Apr 23 2010 Adam Young <ayoung@redhat.com> - 0.3.1-1
- Initial package
