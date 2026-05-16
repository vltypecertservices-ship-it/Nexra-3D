from pathlib import Path
path = Path('public/css/style.css')
text = path.read_text(encoding='utf-8')
old = '''    .footer-logo {
    display: inline-flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 1rem;
}
.footer-logo-image {
    width: 11rem;
    height: auto;
    display: block;
}
.footer-logo span {
    font-size: 1.35rem;
    font-weight: 700;
    color: var(--white);
}
'''
new = '''    .footer-logo {
    display: inline-flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 1rem;
}
.brand-logo,
.footer-logo-image {
    background-color: transparent;
}
.footer-logo-image {
    width: 11rem;
    height: auto;
    display: block;
}
.footer-logo span,
.footer-logo-text {
    font-size: 1.35rem;
    font-weight: 700;
    color: var(--white);
}
'''
if old not in text:
    raise SystemExit('pattern not found')
path.write_text(text.replace(old, new), encoding='utf-8')
