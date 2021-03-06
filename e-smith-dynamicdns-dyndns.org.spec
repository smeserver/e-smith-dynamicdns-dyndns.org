# $Id: e-smith-dynamicdns-dyndns.org.spec,v 1.2 2008/10/07 18:07:49 slords Exp $

Summary: e-smith dynamic dns client to update dyndns.org
%define name e-smith-dynamicdns-dyndns.org
Name: %{name}
%define version 2.2.0
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Utilities
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildRequires: e-smith-devtools
BuildArchitectures: noarch
Requires: e-smith-base, e-smith-lib, e-smith >= 4.1
AutoReqProv: no

%changelog
* Tue Oct 7 2008 Shad L. Lords <slords@mail.com> 2.2.0-1.sme
- Roll new stream to separate sme7/sme8 trees [SME: 4633]

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.4.0-03
- Bump release number only

* Wed May 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-02]
- Add support for "custom", i.e. domain not matching
  *.dyndns.org.

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-01]
- Roll stable version number to 1.4.0

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-01]
- Changing version to maintained stream number to 1.3.0

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.2.3-01]
- RPM rebuild forced by cvsroot2rpm

* Mon Feb 25 2002 Kirrily Robert <skud@e-smith.com>
- [1.2.2-01]
- Testing rpm2cvs

* Mon Feb 25 2002 Kirrily Robert <skud@e-smith.com>
- [1.2.1-01]
- rollRPM: Rolled version number to 1.2.1-01. Includes patches up to 1.2.0-04.

* Fri Aug 17 2001 gordonr
- [1.2.0-04]
- Autorebuild by rebuildRPM

* Fri Jul 6 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-03]
- Changing license to GPL

* Thu Feb  8 2001 Adrian Chung <adrianc@e-smith.com>
- [1.2.0-02]
- Rolling release number for GPG signing.

* Thu Jan 25 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-01]
- Rolled version number to 1.2.0-01. Includes patches upto 1.1.0-2.

* Wed Jan 10 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-2]
- Fix stray backtick, and reformat for 80 char display width

* Tue Jan 9 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-01]
- Rolled version number to 1.1.0-01. Includes patches upto 0.0.1-1

* Sat Jan  6 2001 Charlie Brady <charlieb@e-smith.com>
- initial release

%description
e-smith server dynamic DNS client module to update dyndns.org data

%prep
%setup

%build

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%pre
%preun
%post
%postun

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
