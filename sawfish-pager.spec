%define name sawfish-pager
%define version 0.7.2
%define release %mkrel 1
%define sawfish 1.6.1
%define sfepoch 2

Summary: Lightweight desktop pager for Sawfish
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://sourceforge.net/projects/%name/files/pager/%version/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: Graphical desktop/Sawfish
Url: http://sawfish-pager.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtk+2-devel
BuildRequires: sawfish-devel >= %sfepoch:%sawfish
Requires: sawfish = %sfepoch:%sawfish

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
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc NEWS README TODO
%_libexecdir/sawfish/%sawfish/*/pager
%_datadir/sawfish/%sawfish/lisp/sawfish/wm/ext/pager.jl
