%define	module	POE
%define	name	perl-%{module}
%define	version	1.005
%define	release	%mkrel 1

Name:		%{name}
Epoch:		2
Version:	%{version}
Release:	%{release}
Summary:	Portable multitasking and networking framework for Perl
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/POE/%{module}-%{version}.tar.gz
# This module naming scheme does not follow path names...
Provides:	perl(POE::Resource::Controls)
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildrequires:  perl(Term::ReadKey)
Buildrequires:  perl-libwww-perl
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
POE is a framework for cooperative, event driven multitasking in Perl.

POE originally was developed as the core of a persistent object server and
runtime environment. It has evolved into a general purpose multitasking and
networking framework, encompassing and providing a consistent interface to
other event loops such as Event and the Tk and Gtk toolkits.

POE is a mature framework for creating multitasking programs in Perl.  It has
been in active development since 1998.  It has been used in mission-critical
systems such as internetworked financial markets, file systems, commerce and
application servers.

%prep
%setup -q -n %{module}-%{version}
chmod 755 examples
chmod 755 examples/*.perl

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --default
%make

%check
DISPLAY= %{__make} test

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES HISTORY README examples TODO
%{perl_vendorlib}/POE
%{perl_vendorlib}/*.pm
%{_mandir}/man3/*



