--
-- PostgreSQL database dump
--

-- Dumped from database version 14.13 (Ubuntu 14.13-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.13 (Ubuntu 14.13-0ubuntu0.22.04.1)

-- Started on 2024-11-15 19:38:46 MSK

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO postgres;

--
-- TOC entry 3385 (class 0 OID 0)
-- Dependencies: 3
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 211 (class 1259 OID 16629)
-- Name: comments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.comments (
    id integer NOT NULL,
    text character varying(100) NOT NULL,
    user_id integer NOT NULL,
    post_id integer NOT NULL
);


ALTER TABLE public.comments OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 16650)
-- Name: likes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.likes (
    id integer NOT NULL,
    user_id integer NOT NULL,
    post_id integer NOT NULL
);


ALTER TABLE public.likes OWNER TO postgres;

--
-- TOC entry 213 (class 1259 OID 16640)
-- Name: posts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.posts (
    id integer NOT NULL,
    title character varying(100) NOT NULL,
    description character varying(100) NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.posts OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 16639)
-- Name: posts_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.posts ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.posts_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 210 (class 1259 OID 16624)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying(30) NOT NULL,
    age integer NOT NULL,
    gender character varying(30) NOT NULL,
    nationality character varying(30)
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 16623)
-- Name: users_users_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.users ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.users_users_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 3376 (class 0 OID 16629)
-- Dependencies: 211
-- Data for Name: comments; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.comments (id, text, user_id, post_id) FROM stdin;
1	да ,я тоже считаю audi лучшей по этим  двум параметрам	1	1
2	а я бы лучше в европу бы поехал	1	2
4	С++ намного быстрее фу ваш python)	5	4
5	уже поздно ,эфир берите	3	5
3	нифига надо открывать шаурму	2	3
\.


--
-- TOC entry 3379 (class 0 OID 16650)
-- Dependencies: 214
-- Data for Name: likes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.likes (id, user_id, post_id) FROM stdin;
1	1	3
2	1	5
3	1	1
4	2	1
5	2	3
6	3	5
7	3	3
8	4	4
9	4	3
10	5	1
\.


--
-- TOC entry 3378 (class 0 OID 16640)
-- Dependencies: 213
-- Data for Name: posts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.posts (id, title, description, user_id) FROM stdin;
1	car audi good	audi лучшая мишина по цене и качеству	2
2	travel	ездили семьей в тай.очень понравилось	4
3	business	сейчас лучше всего открывать производство мебели.	3
4	IT	python самый луший язык програмирвания	1
5	cryptocurrency	покупайте биткоин	5
\.


--
-- TOC entry 3375 (class 0 OID 16624)
-- Dependencies: 210
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, name, age, gender, nationality) FROM stdin;
1	valentin	27	man	russian
2	igor	22	man	russian
3	sergey	33	man	russian
4	irina	25	girl	russian
5	bob	33	englander	russian
\.


--
-- TOC entry 3386 (class 0 OID 0)
-- Dependencies: 212
-- Name: posts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.posts_id_seq', 5, true);


--
-- TOC entry 3387 (class 0 OID 0)
-- Dependencies: 209
-- Name: users_users_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_users_seq', 5, true);


--
-- TOC entry 3225 (class 2606 OID 16633)
-- Name: comments comments_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_pk PRIMARY KEY (id);


--
-- TOC entry 3229 (class 2606 OID 16654)
-- Name: likes likes_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_pk PRIMARY KEY (id);


--
-- TOC entry 3227 (class 2606 OID 16644)
-- Name: posts posts_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pk PRIMARY KEY (id);


--
-- TOC entry 3223 (class 2606 OID 16628)
-- Name: users users_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pk PRIMARY KEY (id);


--
-- TOC entry 3231 (class 2606 OID 16645)
-- Name: comments comments_posts_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_posts_fk FOREIGN KEY (post_id) REFERENCES public.posts(id);


--
-- TOC entry 3230 (class 2606 OID 16634)
-- Name: comments comments_users_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_users_fk FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- TOC entry 3234 (class 2606 OID 16660)
-- Name: likes likes_posts_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_posts_fk FOREIGN KEY (post_id) REFERENCES public.posts(id);


--
-- TOC entry 3233 (class 2606 OID 16655)
-- Name: likes likes_users_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_users_fk FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- TOC entry 3232 (class 2606 OID 16665)
-- Name: posts posts_users_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_users_fk FOREIGN KEY (user_id) REFERENCES public.users(id);


-- Completed on 2024-11-15 19:38:47 MSK

--
-- PostgreSQL database dump complete
--

