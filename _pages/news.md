---
layout: page
title: News
permalink: /news/
nav: false
_styles: >
  .post > .post-header { display: none; }
  .news-timeline {
    position: relative;
    margin: 1.5rem 0 2rem;
    padding: 0;
  }
  .news-timeline::before {
    content: "";
    position: absolute;
    left: 7.5rem;
    top: 0.5rem;
    bottom: 0.5rem;
    width: 2px;
    background: linear-gradient(to bottom,
      rgba(2, 132, 199, 0) 0%,
      rgba(2, 132, 199, 0.5) 6%,
      rgba(2, 132, 199, 0.5) 94%,
      rgba(2, 132, 199, 0) 100%);
    z-index: 0;
  }
  @media (max-width: 576px) {
    .news-timeline::before { left: 1.5rem; }
  }

  .news-year {
    position: relative;
    font-size: 1.6rem;
    font-weight: 700;
    color: var(--global-theme-color);
    letter-spacing: 0.02em;
    margin: 1.75rem 0 1.25rem;
    padding-left: 9rem;
    line-height: 1;
  }
  .news-year:first-of-type { margin-top: 0.5rem; }
  .news-year::before {
    content: "";
    position: absolute;
    left: 7rem;
    top: 50%;
    transform: translateY(-50%);
    width: 1.05rem;
    height: 1.05rem;
    border-radius: 50%;
    background: var(--global-theme-color);
    box-shadow: 0 0 0 4px var(--global-bg-color), 0 0 0 5px rgba(2, 132, 199, 0.25);
    z-index: 1;
  }
  @media (max-width: 576px) {
    .news-year { padding-left: 3rem; }
    .news-year::before { left: 1rem; }
  }

  .news-entry {
    position: relative;
    display: flex;
    align-items: stretch;
    gap: 1rem;
    margin: 0.75rem 0;
    padding-left: 0;
  }
  .news-entry-date {
    flex: 0 0 6.5rem;
    text-align: right;
    padding-top: 0.85rem;
    padding-right: 0.25rem;
    font-size: 0.95rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--global-theme-color);
  }

  .news-entry-dot {
    position: relative;
    flex: 0 0 2rem;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .news-entry-dot::after {
    content: "";
    width: 0.9rem;
    height: 0.9rem;
    border-radius: 50%;
    background: var(--global-bg-color);
    border: 2.5px solid var(--global-theme-color);
    z-index: 1;
    transition: transform 0.18s ease, box-shadow 0.18s ease;
  }

  .news-entry-card {
    flex: 1;
    background: var(--global-card-bg-color, var(--global-bg-color));
    border: 1px solid var(--global-divider-color);
    border-left: 3px solid var(--global-theme-color);
    border-radius: 0.6rem;
    padding: 0.85rem 1.1rem;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
    transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
  }
  .news-entry-card p {
    margin: 0;
    font-size: 0.95rem;
    line-height: 1.6;
    color: var(--global-text-color);
  }
  .news-entry-card strong { color: var(--global-theme-color); font-weight: 600; }

  .news-entry:hover .news-entry-card {
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(2, 132, 199, 0.14);
  }
  .news-entry:hover .news-entry-dot::after {
    transform: scale(1.15);
    box-shadow: 0 0 0 4px rgba(2, 132, 199, 0.18);
  }

  /* Tag accents based on emoji-driven theme classes */
  .news-entry.is-award .news-entry-card { border-left-color: #d97706; }
  .news-entry.is-award:hover .news-entry-card { box-shadow: 0 6px 18px rgba(217, 119, 6, 0.18); }
  .news-entry.is-award .news-entry-dot::after { border-color: #d97706; }
  .news-entry.is-award .news-entry-date { color: #b45309; }

  .news-entry.is-paper .news-entry-card { border-left-color: #6366f1; }
  .news-entry.is-paper:hover .news-entry-card { box-shadow: 0 6px 18px rgba(99, 102, 241, 0.18); }
  .news-entry.is-paper .news-entry-dot::after { border-color: #6366f1; }
  .news-entry.is-paper .news-entry-date { color: #4338ca; }

  .news-entry.is-milestone .news-entry-card { border-left-color: #10b981; }
  .news-entry.is-milestone:hover .news-entry-card { box-shadow: 0 6px 18px rgba(16, 185, 129, 0.18); }
  .news-entry.is-milestone .news-entry-dot::after { border-color: #10b981; }
  .news-entry.is-milestone .news-entry-date { color: #047857; }

  @media (max-width: 576px) {
    .news-entry { gap: 0.5rem; }
    .news-entry-date { flex: 0 0 0; padding: 0; display: none; }
    .news-entry-dot { flex: 0 0 1.75rem; }
    .news-entry-card { padding: 0.7rem 0.9rem; }
    .news-entry-card p::before {
      content: attr(data-date);
      display: block;
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--global-theme-color);
      margin-bottom: 0.3rem;
    }
  }

  .news-empty {
    text-align: center;
    padding: 3rem 1rem;
    color: var(--global-text-color-light);
    font-style: italic;
  }
---

{% if site.news != blank %}
{% assign news = site.news | sort: 'date' | reverse %}
{% assign prev_year = "" %}
{% assign prev_ym = "" %}

<div class="news-timeline">
  {% for item in news %}
    {% assign year = item.date | date: '%Y' %}
    {% assign month = item.date | date: '%b' %}
    {% assign ym = item.date | date: '%Y-%m' %}
    {% if year != prev_year %}
      <h2 class="news-year">{{ year }}</h2>
      {% assign prev_year = year %}
    {% endif %}
    {% assign show_month = false %}
    {% if ym != prev_ym %}
      {% assign show_month = true %}
      {% assign prev_ym = ym %}
    {% endif %}
    {% assign content_text = item.content | strip %}
    {% assign theme_class = '' %}
    {% if content_text contains ':trophy:' or content_text contains 'Award' or content_text contains 'Prize' or content_text contains 'Fellowship' %}
      {% assign theme_class = 'is-award' %}
    {% elsif content_text contains ':page_with_curl:' or content_text contains 'paper' or content_text contains 'accepted' or content_text contains 'published' %}
      {% assign theme_class = 'is-paper' %}
    {% elsif content_text contains ':tada:' or content_text contains ':sparkles:' or content_text contains 'joined' or content_text contains 'Joined' %}
      {% assign theme_class = 'is-milestone' %}
    {% endif %}
    <article class="news-entry {{ theme_class }}">
      <div class="news-entry-date">{% if show_month %}{{ month }}{% endif %}</div>
      <div class="news-entry-dot" aria-hidden="true"></div>
      <div class="news-entry-card">
        <p data-date="{{ month }} {{ year }}">{{ item.content | remove: '<p>' | remove: '</p>' | emojify }}</p>
      </div>
    </article>
  {% endfor %}
</div>
{% else %}
<p class="news-empty">No news so far&hellip;</p>
{% endif %}
