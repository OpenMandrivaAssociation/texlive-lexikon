%global tl_name lexikon
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0c
Release:	%{tl_revision}.1
Summary:	Macros for a two language dictionary
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lexikon
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lexikon.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lexikon.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Macros for a two language dictionary

