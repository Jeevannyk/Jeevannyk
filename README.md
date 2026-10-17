<div align="center">

# whoami: Jeevan

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=20&duration=3000&pause=800&color=22C55E&center=true&vCenter=true&width=620&lines=Cybersecurity+%40+NMAMIT;Building+secure+auth+systems;AI%2FML+Security+%7C+Cloud+Security" alt="typing intro" />

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jeevan-nayak-b6663131b/)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:jeevangknayak@gmail.com)

</div>

### status
- Focus: **AI/ML security** and **Azure cloud security**

### payloads

| Project | What it does | Stack |
|---|---|---|
| [**Cipher Auth**](https://github.com/Jeevannyk/REPO_NAME) | Passwordless login via dynamic rotating QR codes, OAuth 2.0 / OIDC | Python, FastAPI |
| [**Dual-Layer Defense**](https://github.com/Jeevannyk/REPO_NAME) | Two-stage AI content safety: regex filtering + LLM semantic analysis | FastAPI, LiteLLM, React |

**Currently exploring:** post-quantum cryptography, home SOC / threat detection, healthcare security systems

### stats

<img align="left" width="49%" src="https://github-readme-stats.vercel.app/api?username=Jeevannyk&show_icons=true&hide_border=true&bg_color=0d1117&title_color=22C55E&icon_color=22C55E&text_color=c9d1d9" alt="GitHub stats" />
<img align="right" width="49%" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Jeevannyk&layout=compact&hide_border=true&bg_color=0d1117&title_color=22C55E&text_color=c9d1d9" alt="Top languages" />

<br clear="both" />

<img src="https://streak-stats.demolab.com?user=Jeevannyk&hide_border=true&background=0d1117&ring=22C55E&fire=22C55E&currStreakLabel=22C55E" alt="GitHub streak" />

### toolchain
**Languages** <br>
<img src="https://skillicons.dev/icons?i=python,c,cpp,js,ts,bash" />

**Backend & Web** <br>
<img src="https://skillicons.dev/icons?i=fastapi,flask,django,react,nextjs,tailwind,sqlite" />

**Platforms & Tools** <br>
<img src="https://skillicons.dev/icons?i=linux,git,docker,azure" />

---

### profile CTF

Find the input that makes `check()` return `1`.

```c
int check(const char *s) {
    const unsigned char k[] = {0x13, 0x37, 0x42};
    const unsigned char t[] = {89,122,59,110,11,53,82,13,57,85,99,
                               125,115,117,47,112,94,67,121,26,83};
    if (strlen(s) != sizeof t) return 0;
    for (int i = 0; i < (int)sizeof t; i++)
        if (((s[i] ^ k[i % 3]) + i) != t[i]) return 0;
    return 1;
}
```

**Submit:** your token is the first 16 hex chars of `sha256("<flag>:<your-github-username>")`

```bash
echo -n 'FLAG_HERE:your-username' | sha256sum | cut -c1-16
```

Then [**open a submission issue**](https://github.com/Jeevannyk/Jeevannyk/issues/new?title=ctf:%20PASTE_TOKEN_HERE) with the title `ctf: <token>`. A bot verifies it and updates the board.

#### solvers
<!-- CTF:START -->
_No solvers yet. Be the first._
<!-- CTF:END -->

---

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Jeevannyk/Jeevannyk/output/github-snake-dark.svg" />
  <img alt="contribution snake" src="https://raw.githubusercontent.com/Jeevannyk/Jeevannyk/output/github-snake.svg" />
</picture>
</div>
