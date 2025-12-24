-- PostgresQL database setup script

-- Enable citext extension for case-insensitive unique columns
create extension if not exists citext;

-- Create users table, create trigger to update updated_at on row modification
create table users (
    id uuid primary key default uuidv7(),
    user_full_name text not null, -- full name of the user
    primary_email citext unique not null, -- email used for login or contact
    primary_email_verified boolean default false, -- verification status
    created_at timestamptz default current_timestamp,
    updated_at timestamptz default current_timestamp
);


create table auth_identities (
    id uuid primary key default uuidv7(),
    user_id uuid references users(id) on delete cascade, -- fk to users table
    provider_type text not null, -- e.g., 'google', 'oauth provider', 'password'
    provider_id text not null, -- e.g. either email or oauth sub
    password_hash text null, -- only for 'password' provider_type
    display_email text, -- display purposes only email, cannot be used to login
    created_at timestamptz default current_timestamp,
    updated_at timestamptz default current_timestamp,
    unique(provider_type, provider_id), -- No two people can share a google email
    unique(user_id, provider_type) -- User cannot have two auth identities of the same type, natural key
);
-- Index to speed up lookups by user_id
create index idx_auth_identities_user_id on auth_identities(user_id);

-- Trigger function to update updated_at column on row modification
create function update_updated_at_column()
returns trigger as $$
begin
    new.updated_at = current_timestamp;
    return new;
end;
$$ language 'plpgsql';

-- Create triggers for users and auth_identities tables
create trigger update_users_updated_at
    before update on users
    for each row
    execute function update_updated_at_column();

-- Create trigger for auth_identities table
create trigger update_auth_identities_updated_at
    before update on auth_identities
    for each row
    execute function update_updated_at_column();
