#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pname	Octave
Summary:	Inline::Octave Perl module
Summary(cs):	Modul Inline::Octave pro Perl
Summary(da):	Perlmodul Inline::Octave
Summary(de):	Inline::Octave Perl Modul
Summary(es):	Módulo de Perl Inline::Octave
Summary(fr):	Module Perl Inline::Octave
Summary(it):	Modulo di Perl Inline::Octave
Summary(ja):	Inline::Octave Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Inline::Octave ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Inline::Octave
Summary(pl):	Modu³ Perla Inline::Octave
Summary(pt):	Módulo de Perl Inline::Octave
Summary(pt_BR):	Módulo Perl Inline::Octave
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Inline::Octave
Summary(sv):	Inline::Octave Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Inline::Octave
Summary(zh_CN):	Inline::Octave Perl Ä£¿é
Name:		perl-Inline-Octave
Version:	0.16
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Inline >= 0.4
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	octave
Requires:	octave
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Octave - Inline octave code into your perl.

%description -l pl
Modu³ Inline::Octave - pozwalaj±cy na umieszczanie kodu w jêzyku
Octave w skryptach perlowych.

%prep
%setup -q -n %{pdir}-%{pname}-%{version}

%build
echo '/usr/bin/octave' | perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/Inline/Octave.pm
%{_mandir}/man3/*
