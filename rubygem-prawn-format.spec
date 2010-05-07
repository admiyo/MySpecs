# Generated from prawn-format-0.2.3.gem by gem2rpm -*- rpm-spec -*-
%global ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname prawn-format
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: an extension of Prawn that allows inline formatting
Name: rubygem-%{gemname}
Version: 0.2.3
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://rubyforge.org/projects/prawn
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby(abi) = 1.8
Requires: rubygems
Requires: rubygem(prawn-core) >= 0
Requires: rubygem(echoe) >= 0
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
an extension of Prawn that allows inline formatting


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
%doc %{geminstdir}/lib/prawn/format/effects/link.rb
%doc %{geminstdir}/lib/prawn/format/effects/underline.rb
%doc %{geminstdir}/lib/prawn/format/instructions/base.rb
%doc %{geminstdir}/lib/prawn/format/instructions/tag_close.rb
%doc %{geminstdir}/lib/prawn/format/instructions/tag_open.rb
%doc %{geminstdir}/lib/prawn/format/instructions/text.rb
%doc %{geminstdir}/lib/prawn/format/layout_builder.rb
%doc %{geminstdir}/lib/prawn/format/lexer.rb
%doc %{geminstdir}/lib/prawn/format/line.rb
%doc %{geminstdir}/lib/prawn/format/parser.rb
%doc %{geminstdir}/lib/prawn/format/state.rb
%doc %{geminstdir}/lib/prawn/format/text_object.rb
%doc %{geminstdir}/lib/prawn/format/version.rb
%doc %{geminstdir}/lib/prawn/format.rb
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Wed Mar 31 2010 Adam Young <ayoung@ayoung.boston.devel.redhat.com> - 0.2.3-1
- Initial package
