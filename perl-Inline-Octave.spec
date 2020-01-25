#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Inline
%define		pnam	Octave
Summary:	Inline::Octave - inline octave code into your perl
Summary(pl.UTF-8):	Inline::Octave - umieszczanie kodu octave w kodzie perlowym
Name:		perl-Inline-Octave
Version:	0.20
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4c590abe9d4073cc35a3ad8a6322c763
Patch0:		%{name}-test.patch
URL:		http://search.cpan.org/dist/Inline-Octave/
BuildRequires:	octave
BuildRequires:	perl-Inline >= 0.4
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	octave
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Octave Perl module gives you the power of the octave
programming language from within your Perl programs.

%description -l pl.UTF-8
Moduł Perla Inline::Octave umożliwia korzystanie z mocy języka
programowania octave wewnątrz skryptów w Perlu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
echo '/usr/bin/octave' | perl Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Inline/Octave.pm
%{_mandir}/man3/*
