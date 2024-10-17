%define name sawfish-pager
%define version 0.90.3
%define release 2
%define sawfish 1.8.1
%define sfepoch 2
%define sfver %(rpm -q sawfish --queryformat %{VERSION})

Summary: Lightweight desktop pager for Sawfish
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://download.tuxfamily.org/sawfishpager/%name-%version.tar.xz
License: GPLv2+
Group: Graphical desktop/Sawfish
Url: https://sawfish-pager.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtk+2-devel
BuildRequires: sawfish-devel >= %sfepoch:%sawfish
Requires: sawfish >= %sfepoch:%sfver

%description
A pager is a map of your desktop. As maps go, it shows not only the visible
part (your current viewport), but if you are so configured, also the parts
that extend beyond the sides of your screen. Also, if you have more than
one workspace, the pager will follow you to where you are, or optionally
show all workspaces at once. Of course you can select viewports and
windows, and also move or raise/lower the latter.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc NEWS README TODO
%_libexecdir/sawfish/sawfishpager
%_datadir/sawfish/lisp/sawfish/wm/ext/pager.jl
%_datadir/sawfish/lisp/sawfish/wm/ext/pager.jlc



%changelog
* Wed Mar 28 2012 Götz Waschk <waschk@mandriva.org> 0.90.3-1mdv2012.0
+ Revision: 788007
- new version

* Wed May 04 2011 Götz Waschk <waschk@mandriva.org> 0.90.2-1
+ Revision: 665834
- new version
- update file list
- relax sawfish dep

* Mon May 02 2011 Götz Waschk <waschk@mandriva.org> 0.90.1-2
+ Revision: 662164
- rebuild with new sawfish
- update file list

* Wed Mar 30 2011 Götz Waschk <waschk@mandriva.org> 0.90.1-1
+ Revision: 649044
- new version
- bump sawfish dep

* Fri Dec 17 2010 Götz Waschk <waschk@mandriva.org> 0.90.0-1mdv2011.0
+ Revision: 622507
- new version
- update file list
- bump sawfish dep

* Sun Jul 11 2010 Götz Waschk <waschk@mandriva.org> 0.7.4-1mdv2011.0
+ Revision: 550829
- update to new version 0.7.4

* Tue Feb 16 2010 Götz Waschk <waschk@mandriva.org> 0.7.3-1mdv2010.1
+ Revision: 506624
- new version
- fix source URL
- fix build
- fix binary package dep on sawfish

* Sat Jan 09 2010 Götz Waschk <waschk@mandriva.org> 0.7.2-1mdv2010.1
+ Revision: 488107
- import sawfish-pager


* Sat Jan  9 2010 Götz Waschk <waschk@mandriva.org> 0.7.2-1mdv2010.1
- initial package
