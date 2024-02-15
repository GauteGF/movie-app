"use client";

import Link from "next/link";

export default function Banner() {
    return (
        <div className="w-full bg-blue-500 h-[500px]">
            <Link href={"/"}>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-10 h-10">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 19.5 8.25 12l7.5-7.5" />
                </svg>
            </Link>
            <p>This is a temporary m</p>
        </div>

    )
}