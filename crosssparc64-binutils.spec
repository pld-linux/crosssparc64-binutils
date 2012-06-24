Summary:	GNU Binary Utility Development Utilities
Summary(de):	GNU Binary Utility Development Utilities
Summary(es):	Utilitarios para desarrollo de binarios de la GNU
Summary(fr):	Utilitaires de d�veloppement binaire de GNU
Summary(pl):	Narz�dzia GNU dla programist�w
Summary(pt_BR):	Utilit�rios para desenvolvimento de bin�rios da GNU
Summary(tr):	GNU geli�tirme ara�lar�
Name:		crosssparc64-binutils
Version:	2.11.92.0.12.3
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.kernel.org/pub/linux/devel/binutils/binutils-%{version}.tar.bz2
URL:		http://sourceware.cygnus.com/binutils/
Prereq:		/sbin/ldconfig
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	perl-devel
BuildRequires:	bash
%ifarch sparc sparc32
BuildRequires:	sparc32
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target		sparc64-pld-linux
%define		arch		%{_prefix}/%{target}

%description
Binutils is a collection of binary utilities, including:
- ar - create, modify and extract from archives,
- nm - lists symbols from object files,
- objcopy - copy and translate object files,
- objdump - display information from object files,
- ranlib - generate an index for the contents of an archive,
- size - list the section sizes of an object or archive file,
- strings - list printable strings from files,
- strip - discard symbols,
- c++filt - a filter for demangling encoded C++ symbols,
- addr2line - convert addresses to file and line,
- nlmconv - convert object code into an NLM.

Cross version for SPARC64

%description -l pl
Pakiet binutils zawiera zestaw narz�dzi umo�liwiaj�cych kompilacj�
program�w. Znajduj� si� tutaj mi�dzy innymi assembler, konsolidator
(linker), a tak�e inne narz�dzia do manipulowania binarnymi plikami
program�w i bibliotek.

Wersja cross generuj�ca dla SPARC64

%prep
%setup -q -n binutils-%{version}

%build
# ldscripts won't be generated properly if SHELL is not bash...
CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" \
CONFIG_SHELL="/bin/bash" \
%ifarch sparc
sparc32 \
%endif
./configure \
	--disable-shared \
	--prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--target=%{target}

%{__make} tooldir=%{_prefix} EXEEXT="" all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

# remove these man pages unless we cross-build for win*/netware platforms.
# however, this should be done in Makefiles.
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/{*dlltool,*nlmconv,*windres}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{target}-*
%dir %{arch}/bin
%attr(755,root,root) %{arch}/bin/*
%dir %{arch}/lib
%dir %{arch}/lib/*
%{_mandir}/man?/%{target}-*
