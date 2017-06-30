# Generated from domain_name-0.5.20170404.gem by gem2rpm -*- rpm-spec -*-
%global gem_name domain_name

Name:           rubygem-%{gem_name}
Version:        0.5.20170404
Release:        2%{?dist}
Summary:        Domain Name manipulation library for Ruby
Group:          Development/Languages
License:        BSD and (MPLv1.1 or GPLv2+ or LGPLv2+) 
URL:            https://github.com/knu/ruby-domain_name
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby
# BuildRequires: rubygem(test-unit) >= 2.5.5
# BuildRequires: rubygem(test-unit) < 2.6
BuildArch:      noarch
Provides:       rubygem(%{gem_name}) = %{version}

%description
This is a Domain Name manipulation library for Ruby.
It can also be used for cookie domain validation based on the Public
Suffix List.


%package doc
Summary:        Documentation for %{name}
Group:          Documentation
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

sed -i -e 's/\/usr\/bin\/env ruby/\/usr\/bin\/ruby/g' %{gem_name}-%{version}/tool/gen_etld_data.rb
chmod 744 %{gem_name}-%{version}/tool/gen_etld_data.rb

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_libdir}
%{gem_spec}

%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/data
%exclude %{gem_instdir}/domain_name.gemspec
%exclude %{gem_instdir}/tool
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%license %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/.document
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Tue Jun 20 2017 Juan Badia Payno <jbadiapa@redhat.com> - 0.5.20170404-2
- 0.5.20170404 package for CentOS

* Fri May  5 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.20170404-1
- 0.5.20170404

* Tue Mar 14 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.20170223-1
- 0.5.20170223

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.20161129-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 31 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.20161129-1
- 0.5.20161129

* Fri Nov 18 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.20161021-1
- 0.5.20161021

* Sat Sep 10 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.20160826-1
- 0.5.20160826

* Thu Jun 30 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.20160615-1
- 0.5.20160615

* Mon Mar 28 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.20160310-1
- 0.5.20160310

* Mon Mar 14 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.20160309-1
- 0.5.20160309

* Wed Mar  9 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.20160216-1
- 0.5.20160216

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.20160128-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb  1 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.20160128-1
- 0.5.20160128

* Thu Oct  8 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.25-1
- 0.5.25

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 17 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.24-1
- 0.5.24

* Sun Dec 21 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.23-1
- 0.5.23

* Tue Nov  4 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.22-1
- 0.5.22

* Wed Sep 10 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.21-1
- 0.5.21

* Sun Aug 31 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.20-1
- 0.5.20

* Fri Jun 27 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.19-1
- 0.5.19

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 08 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.18-2
- Support Minitest 5+

* Mon Apr 07 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.18-1
- 0.5.18

* Sat Feb 15 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.16-1
- 0.5.16

* Tue Nov 19 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.15-1
- 0.5.15

* Tue Oct 22 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.14-1
- 0.5.14

* Fri Oct 11 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.13-2
- Remove redundant BR

* Tue Oct  8 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.13-1
- 0.5.13

* Mon Apr 29 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.11-1
- 0.5.11

* Fri Mar 22 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.9-1
- 0.5.9

* Sun Jan 27 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.7-2
- A bit clean up

* Sun Jan 27 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.7-1
- Initial package

