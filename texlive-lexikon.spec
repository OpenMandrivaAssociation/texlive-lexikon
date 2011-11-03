# revision 17364
# category Package
# catalog-ctan /macros/latex/contrib/lexikon
# catalog-date 2010-03-06 21:34:04 +0100
# catalog-license lppl
# catalog-version 1.0c
Name:		texlive-lexikon
Version:	1.0c
Release:	1
Summary:	Macros for a two language dictionary
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lexikon
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lexikon.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lexikon.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive lexikon package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lexikon/lexikon.sty
%doc %{_texmfdistdir}/doc/latex/lexikon/lexikon-doc.pdf
%doc %{_texmfdistdir}/doc/latex/lexikon/lexikon-doc.tex
%doc %{_texmfdistdir}/doc/latex/lexikon/lexikon.tex
%doc %{_texmfdistdir}/doc/latex/lexikon/lexikon.upl
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
