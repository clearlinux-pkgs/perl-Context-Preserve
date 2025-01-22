#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Context-Preserve
Version  : 0.03
Release  : 26
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Context-Preserve-0.03.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Context-Preserve-0.03.tar.gz
Summary  : 'Run code after a subroutine call, preserving the context the subroutine would have seen if it were the last statement in the caller'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Context-Preserve-license = %{version}-%{release}
Requires: perl-Context-Preserve-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Exception)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution Context-Preserve,
version 0.03:
Run code after a subroutine call, preserving the context the subroutine would have seen if it were the last statement in the caller

%package dev
Summary: dev components for the perl-Context-Preserve package.
Group: Development
Provides: perl-Context-Preserve-devel = %{version}-%{release}
Requires: perl-Context-Preserve = %{version}-%{release}

%description dev
dev components for the perl-Context-Preserve package.


%package license
Summary: license components for the perl-Context-Preserve package.
Group: Default

%description license
license components for the perl-Context-Preserve package.


%package perl
Summary: perl components for the perl-Context-Preserve package.
Group: Default
Requires: perl-Context-Preserve = %{version}-%{release}

%description perl
perl components for the perl-Context-Preserve package.


%prep
%setup -q -n Context-Preserve-0.03
cd %{_builddir}/Context-Preserve-0.03

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Context-Preserve
cp %{_builddir}/Context-Preserve-%{version}/LICENCE %{buildroot}/usr/share/package-licenses/perl-Context-Preserve/973aaa05e5ca98e0c9a650dfbb020c7324946df6 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Context::Preserve.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Context-Preserve/973aaa05e5ca98e0c9a650dfbb020c7324946df6

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
