<div align="center">

# Hi, I'm Jeevan 👋

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=20&duration=3000&pause=800&color=22C55E&center=true&vCenter=true&width=620&lines=Cybersecurity+%40+NMAMIT;Building+secure+auth+systems;AI%2FML+Security+%7C+Cloud+Security" alt="typing intro" />

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jeevan-nayak-b6663131b/)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:jeevangknayak@gmail.com)

</div>

### 🛡️ Now
- B.Tech CSE (Cybersecurity) @ NMAMIT, 2024-2028
- Working toward **SC-500** (Cloud & AI Security Engineer)
- Focus: **AI/ML security** and **Azure cloud security**

### 🔬 Featured Work

| Project | What it does | Stack |
|---|---|---|
| [**Cipher Auth**](https://github.com/Jeevannyk/REPO_NAME) | Passwordless login via dynamic rotating QR codes, OAuth 2.0 / OIDC | Python, FastAPI |
| [**Dual-Layer Defense**](https://github.com/Jeevannyk/REPO_NAME) | Two-stage AI content safety: regex filtering + LLM semantic analysis | FastAPI, LiteLLM, React |
| **Network IDS Research** (MAHE-ISAC) | 5.56M+ traffic records, 14 attack classes, SHAP feature selection, CTGAN + SMOTE, **0.7631 Macro-F1**, served via FastAPI | XGBoost, LightGBM, FastAPI |


### 🧰 Stack
**Languages** <br>
<img src="https://skillicons.dev/icons?i=python,c,cpp,js,ts,bash" />

**Backend & Web** <br>
<img src="https://skillicons.dev/icons?i=fastapi,flask,django,react,nextjs,tailwind,sqlite" />

**Platforms & Tools** <br>
<img src="https://skillicons.dev/icons?i=linux,git,docker,azure" />

---

### 🚩 Profile CTF

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

#### 🏁 Solvers
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
