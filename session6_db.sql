--
-- PostgreSQL database dump
--

-- Dumped from database version 14.4
-- Dumped by pg_dump version 14.4

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: plants; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.plants (
    id integer NOT NULL,
    name character varying,
    scientific_name character varying,
    is_poisonous boolean,
    primary_color character varying,
    state character varying NOT NULL
);


ALTER TABLE public.plants OWNER TO postgres;

--
-- Name: plants_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.plants ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.plants_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: plants; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.plants (id, name, scientific_name, is_poisonous, primary_color, state) FROM stdin;
2	Papaye	Carica papaya	f	green	Togo
4	Citron	Citrus limon	f	yellow	Ghana
5	Anacardier	Anacardium occidentale	f	yellow	Ghana
6	Anacardier	Anacardium occidentale	f	yellow	Ghana
7	Anacardier	Anacardium occidentale	f	yellow	Ghana
8	Anacardier	Anacardium occidentale	f	yellow	Ghana
9	Anacardier	Anacardium occidentale	f	yellow	Ghana
10	Anacardier	Anacardium occidentale	f	yellow	Ghana
11	Anacardier	Anacardium occidentale	f	yellow	Ghana
12	Anacardier	Anacardium occidentale	f	yellow	Ghana
13	Anacardier	Anacardium occidentale	f	yellow	Ghana
14	Anacardier	Anacardium occidentale	f	yellow	Ghana
15	Anacardier	Anacardium occidentale	f	yellow	Ghana
16	Anacardier	Anacardium occidentale	f	yellow	Ghana
18	Anacardier	Anacardium occidentale	f	yellow	Ghana
19	Anacardier	Anacardium occidentale	f	yellow	Ghana
20	Anacardier	Anacardium occidentale	f	yellow	Ghana
21	Anacardier	Anacardium occidentale	f	yellow	Ghana
22	Anacardier	Anacardium occidentale	f	yellow	Ghana
23	Anacardier	Anacardium occidentale	f	yellow	Ghana
24	Anacardier	Anacardium occidentale	f	yellow	Ghana
25	Anacardier	Anacardium occidentale	f	yellow	Ghana
26	Anacardier	Anacardium occidentale	f	yellow	Ghana
27	Anacardier	Anacardium occidentale	f	yellow	Ghana
28	Anacardier	Anacardium occidentale	f	yellow	Ghana
29	Anacardier	Anacardium occidentale	f	yellow	Ghana
30	Anacardier	Anacardium occidentale	f	yellow	Ghana
31	Anacardier	Anacardium occidentale	f	yellow	Ghana
32	Anacardier	Anacardium occidentale	f	yellow	Ghana
1	Avocat	Persea americana	f	black	Togo
\.


--
-- Name: plants_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.plants_id_seq', 32, true);


--
-- Name: plants plants_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.plants
    ADD CONSTRAINT plants_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

