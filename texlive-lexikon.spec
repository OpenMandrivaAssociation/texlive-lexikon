Name:		texlive-lexikon
Version:	17364
Release:	2
Summary:	Macros for a two language dictionary
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lexikon
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lexikon.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lexikon.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive lexikon package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lexikon/lexikon.sty
%doc %{_texmfdistdir}/doc/latex/lexikon/lexikon-doc.pdf
%doc %{_texmfdistdir}/doc/latex/lexikon/lexikon-doc.tex
%doc %{_texmfdistdir}/doc/latex/lexikon/lexikon.tex
%doc %{_texmfdistdir}/doc/latex/lexikon/lexikon.upl

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
