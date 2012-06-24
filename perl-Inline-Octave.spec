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
Summary(es):	M�dulo de Perl Inline::Octave
Summary(fr):	Module Perl Inline::Octave
Summary(it):	Modulo di Perl Inline::Octave
Summary(ja):	Inline::Octave Perl �⥸�塼��
Summary(ko):	Inline::Octave �� ����
Summary(no):	Perlmodul Inline::Octave
Summary(pl):	Modu� Perla Inline::Octave
Summary(pt):	M�dulo de Perl Inline::Octave
Summary(pt_BR):	M�dulo Perl Inline::Octave
Summary(ru):	������ ��� Perl Inline::Octave
Summary(sv):	Inline::Octave Perlmodul
Summary(uk):	������ ��� Perl Inline::Octave
Summary(zh_CN):	Inline::Octave Perl ģ��
Name:		perl-Inline-Octave
Version:	0.17
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Inline >= 0.4
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	octave
Requires:	octave
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Octave - Inline octave code into your perl.

%description -l pl
Modu� Inline::Octave - pozwalaj�cy na umieszczanie kodu w j�zyku
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
%{perl_vendorlib}/Inline/Octave.pm
%{_mandir}/man3/*
