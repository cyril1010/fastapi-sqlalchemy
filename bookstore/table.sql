CREATE TABLE public.bookstore
(
    id serial NOT NULL,
    title text,
    author text,
    genre text,
    price numeric,
    stock integer,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.bookstore
    OWNER to postgres;

ALTER TABLE IF EXISTS public.bookstore
    ADD COLUMN created timestamp without time zone DEFAULT CURRENT_TIMESTAMP;

ALTER TABLE IF EXISTS public.bookstore
    ADD COLUMN active boolean DEFAULT true;