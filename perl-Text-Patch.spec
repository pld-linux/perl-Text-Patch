#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Text
%define		pnam	Patch
%include	/usr/lib/rpm/macros.perl
Summary:	Text::Patch - Patches text with given patch
Name:		perl-%{pdir}-%{pnam}
Version:	1.8
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ad5e453d5ba3b48afd8163114d0fee1c
URL:		http://search.cpan.org/dist/%{pdir}-%{pnam}/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Text-Diff
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Patch combines source text with given diff (difference) data.
Diff data is produced by Text::Diff module or by the standard diff
utility (man diff, see -u option).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
