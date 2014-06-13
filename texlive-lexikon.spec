# revision 17364
# category Package
# catalog-ctan /macros/latex/contrib/lexikon
# catalog-date 2010-03-06 21:34:04 +0100
# catalog-license lppl
# catalog-version 1.0c
Name:		texlive-lexikon
Version:	1.0c
Release:	7
Summary:	Macros for a two language dictionary
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lexikon
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lexikon.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lexikon.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0c-2
+ Revision: 753297
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0c-1
+ Revision: 718849
- texlive-lexikon
- texlive-lexikon
- texlive-lexikon
- texlive-lexikon

